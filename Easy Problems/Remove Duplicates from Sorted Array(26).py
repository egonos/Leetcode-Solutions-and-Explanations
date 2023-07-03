"""
Intuition
Hi everyone! For this problem, I used remove for inplace replacement. To use it correctly I initiated a while loop. If the current index has the same value with the previous index then it removes it from list and does not increase the index. Otherwise, I increase the index by one.

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        while pointer < len(nums): 
            if nums[pointer-1] == nums[pointer]: nums.remove(nums[pointer])
            else: pointer+=1

        return pointer