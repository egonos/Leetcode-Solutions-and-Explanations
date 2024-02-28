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

        self.max_depth = 0

        def dfs(root):
            if not root:
                return 0

            leftdepth = dfs(root.left)
            rightdepth = dfs(root.right)

            self.max_depth = max(self.max_depth, leftdepth + rightdepth)
            return max(leftdepth,rightdepth) + 1

        dfs(root)

        return self.max_depth