"""
Intuition
The key point of this question is that the good condition depends on exceeding the maximum value through the path (not global maximum value). So defining maximum variable as a global variable does not give use the correct result. Instead, we should include the maximum value in the recursive function.

Approach
After implementing classical DFS approach, we should compare the node's value with the maximum value. If it is greater or equal to the maximum value, we increase the global variable self.count by one.

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
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def counter(node, max_val):
            if not node: 
                return
            
            if node.val >= max_val: 
                self.count += 1
                max_val = node.val

            counter(node.left, max_val)
            counter(node.right, max_val)

        counter(root, root.val)

        return self.count