"""
Intuition
Hi everyone! For this problem, I've utilized dynamic programming approach. The whole code tries maximize the profit based on this condition: We can choose current home and two homes prior or one house before.

dp[1] = max(dp[0],nums[1])
dp[i] = max(dp[i-1],nums[i]+dp[i-2])

Complexity

Time complexity:
-> Loop: O(n)
Space complexity:
-> Array: O(n)

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1: return nums[0]
        elif n == 2: return max(nums)

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])

        return dp[-1]