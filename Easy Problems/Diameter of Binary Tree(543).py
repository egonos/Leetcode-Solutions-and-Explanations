"""
Approach
The algorithm uses DFS to traverse the tree. In each recursion it takes maximum depth of left and right
then compares it with the maximum diameter encountered so far.

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def compute_diameter(node):
            if not node: return 0
            left = compute_diameter(node.left)
            right = compute_diameter(node.right)

            self.diameter = max(self.diameter,left+right)

            return max(left,right)+1

        compute_diameter(root)

        return self.diameter