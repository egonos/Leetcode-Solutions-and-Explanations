"""
Intuition
Hi everyone! For this problem, first I've used traditional DFS approach to find the node we are looking for. Then in the second one, I've utilized the a property of BST :

Smaller values are placed on the left branch and bigger values are placed on the right branch. (Compared to the parent node of course)

Here is my first solution
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):
            if not node: return node
            if node.val == val: return node 

            left = search(node.left)
            right = search(node.right)
            if left: return left
            if right: return right
            


            
        return search(root) 

"""
and here is the second one:
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):
            if not node: return node
            if node.val == val: return node 

            if val < node.val: return search(node.left)
            elif val > node.val: return search(node.right)

        
        return search(root)