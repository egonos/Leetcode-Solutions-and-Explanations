"""
Approach
Define a recursive function to split left and right arrays and add new nodes to the Tree having the max values of left_array and right_array to the left and right childs respectively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(lst):
            if not lst: return

            max_val = max(lst)
            max_idx = lst.index(max_val)
            node = TreeNode(val = max_val)
            left_array = lst[:max_idx]
            right_array = lst[max_idx+1:]

            node.left = construct(left_array)
            node.right = construct(right_array)

            return node


        return construct(nums)