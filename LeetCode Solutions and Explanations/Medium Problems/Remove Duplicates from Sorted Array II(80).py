class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        memory = set()
        while pointer < len(nums):
            if pointer < len(nums) - 1 and nums[pointer] == nums[pointer + 1] and nums[pointer] not in memory:
                memory.add(nums[pointer])
            
            elif pointer < len(nums) - 1 and nums[pointer] == nums[pointer + 1] and nums[pointer] in memory:
                while pointer < len(nums) - 1 and nums[pointer] == nums[pointer+1]:
                    nums.pop(pointer + 1)

            pointer += 1

        return len(nums)