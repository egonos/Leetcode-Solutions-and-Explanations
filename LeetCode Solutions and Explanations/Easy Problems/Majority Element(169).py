class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        record_dict = {}
        for num in nums:
            if num not in record_dict:
                record_dict[num] = 1

            else:
                record_dict[num] += 1

            if record_dict[num] > n:
                return num