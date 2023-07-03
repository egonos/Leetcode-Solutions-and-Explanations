"""
Approach
Similar to the preorder traversal, we have to define a recursive function which stores the values in the following order:

Postorder Traversal

->Left child
->Right child
->Root

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # List to store the postorder traversal

        def postorder(node):
            if not node:
                return

            postorder(node.left)  
            postorder(node.right)  
            result.append(node.val)  

        postorder(root)  
        return result  