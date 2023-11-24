"""
Approach
We can define a function which recursively controls all the nodes across the tree. If it finds an imbalance it returns -1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node: 
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return get_height(root) != -1