"""
Intuition
Hi everyone! For this problem I've used dynamic programming method. The array I've created iteratively adds the altitude by following the pattern.

Complexity
Time complexity:
-> Loop: O(n)

Space complexity:
-> Array: O(n)

"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        dp = [0]
        for i in range(len(gain)): dp.append(dp[i]+gain[i])
        return max(dp)