"""
Approach
Define a recursive function to recursively follow the Inorder Traversal.

Inorder Traversal:
->Left child
->Parent node
->Right child

Complexity
Time complexity:
Space complexity:

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def inorder(node):
            if not node: return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right)


        inorder(root)

        return lst