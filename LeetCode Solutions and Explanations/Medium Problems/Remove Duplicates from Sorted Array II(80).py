"""
Intuition
Hi everyone! For this question, I followed a similar strategy with the easier one. The only difference is that I employed a boolean variable to check duplicate values.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        duplicate = False
        while pointer<len(nums):
            if not duplicate and nums[pointer] == nums[pointer-1]:
                duplicate = True
                pointer+=1

            elif duplicate and nums[pointer] == nums[pointer-1]:
                nums.remove(nums[pointer])

            else:
                duplicate = False
                pointer+=1

        return len(nums)