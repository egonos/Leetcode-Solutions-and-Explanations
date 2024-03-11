# Brute Force Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_idx in range(len(nums)):
            for second_idx in range(first_idx + 1,len(nums)):
                if sum([nums[first_idx], nums[second_idx]]) == target:
                    return [first_idx,second_idx]

# 2nd Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            complementary = target - nums[i]

            if complementary in dic:
                return dic[complementary],i

            else:
                dic[nums[i]] = i