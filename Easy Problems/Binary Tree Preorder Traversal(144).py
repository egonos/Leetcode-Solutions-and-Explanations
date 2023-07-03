"""
Approach
we can write a recursive function to apply preorder traversal through all the nodes.

Preorder traversal:
->Node's value itself
->Node's left value
->Node's right value
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []

        def preorder(node):
            if not node: return 
            self.result.append(node.val)
            preorder(node.left)
            preorder(node.right)


        preorder(root)
        return self.result