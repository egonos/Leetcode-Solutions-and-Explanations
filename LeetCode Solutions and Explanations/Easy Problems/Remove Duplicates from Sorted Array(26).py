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