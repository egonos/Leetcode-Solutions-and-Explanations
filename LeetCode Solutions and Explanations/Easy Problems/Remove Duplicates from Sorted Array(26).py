"""
Intuition
Hi everyone! For this problem, I used remove for inplace replacement. To use it correctly I initiated a while loop. If the current index has the same value with the previous index then it removes it from list and does not increase the index. Otherwise, I increase the index by one.

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        pointer = 0
        while pointer < len(nums):
            if pointer < len(nums) -1 and nums[pointer] == nums[pointer+1]:
                nums.pop(pointer + 1)

            else:
                pointer +=1

        return len(nums)