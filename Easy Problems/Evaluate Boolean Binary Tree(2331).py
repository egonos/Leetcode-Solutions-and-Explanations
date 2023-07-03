"""
Approach
This problem can be solved using a recursive DFS.

I used the eval() function to traverse the tree. If the current node is a leaf, then the function returns its boolean value.

If the node is not a leafi the algorithm recursively calls eval() on its left and right children to compute their boolean values. Then it checks the value of the current node. If it's 2, it returns OR of the children's values, and if it's 3, it returns AND of the children's values.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(node):
            if not node.left and not node.right:
                return bool(node.val)

            if not node:
                return False

            left = eval(node.left)
            right = eval(node.right)

            

            if node.val == 2:
                return left or right
            if node.val == 3:
                return left and right

        return eval(root)