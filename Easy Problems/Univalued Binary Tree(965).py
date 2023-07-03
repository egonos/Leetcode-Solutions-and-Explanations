"""
Approach
We can define a recursive function to implemet DFS. During the traversal if the value of the given node is not equal to the value of the root, then the function immediately returns False. If there are not nodes to traverse it returns True.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        value = root.val 

        if root and not root.left and not root.right:
            return True

        def control(node):
            if not node: return True
            if node.val != value: return False
                
            

            left = control(node.left)
            right = control(node.right)
            

            return left and right


        return control(root)