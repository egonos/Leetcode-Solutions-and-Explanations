"""
Approach
My approach is to utilize BFS algorithm and save the sum of the values in a dict() object. Then I sorted them based on their summation values and returned smallest level.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    
        storage = deque()
        storage.append((1,root))
        sum_level = {}

        while storage:
            depth,node = storage.popleft()
            if depth not in sum_level: sum_level[depth] = node.val
            else: sum_level[depth] +=node.val
            if node.left:
                storage.append((depth+1,node.left))
            if node.right:
                storage.append((depth+1,node.right))

        return sorted(sum_level.items(), key = lambda x: (-x[1],x[0]))[0][0]