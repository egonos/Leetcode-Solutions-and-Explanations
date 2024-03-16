class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = [0] * (len(nums) + 1)
        maxMoney[1] = nums[0]
        for i in range(2,len(nums)+1):
            maxMoney[i] = max(maxMoney[i-1],maxMoney[i-2] + nums[i-1])

        return maxMoney[-1]