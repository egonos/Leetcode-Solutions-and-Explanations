"""
Intuition
Hi everyone! For this problem I've utilized the stack approach. First, I've sorted the input nums then append and pop the values from the stack to find the unique one.

Complexity
Time complexity:
Sorting: O(nlog n)
Looping: O(n)
Resulting: O(nlog n)

Space complexity: O(n)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        stack = []
        for i in range(len(nums)):
            if stack and stack[-1] == nums[i]: stack.pop()
            else: stack.append(nums[i])

        return stack[0]