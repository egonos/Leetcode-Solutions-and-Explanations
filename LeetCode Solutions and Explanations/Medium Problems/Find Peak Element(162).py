"""
Intuition
Hi everyone! This is my way to solve this problem. I'm sure that there are more optimized solutions out there so before looking this solution, if you are searching for the best one I suggest to check the other solutions.

Approach
My approach is to slide a window to handle all the charachters except the first and the last. For the remaining indexes and special conditions, I used conditional statements:

if n == 1: return 0: Arrays with single length.
if n == 2: return nums.index(max(nums)): Arrays with length of 2.
if nums[0]>nums[1]: return 0: 0th index
if nums[-1]>nums[-2]: return n-1Last index

Complexity
Time complexity:
-> Loop O(n)

Space complexity:
->O(1)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if n == 2: return nums.index(max(nums))
        if nums[0]>nums[1]: return 0
        
        for i in range(1,n-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i

            else:
                pass



        if nums[-1]>nums[-2]: return n-1

        
