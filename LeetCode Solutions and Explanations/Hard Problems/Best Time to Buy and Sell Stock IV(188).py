"""
Intuition
Hi everyone! For the last couple of hours, I was working on this problem. I hope what I understood will be helpful to you. If you want to add something please do so. I would be really happy if I learned something from you.

Now our aim is similar to the other varients of Buy-Sell Stocks problems. The only difference is the number of transactions are semi-limited. For that reason we have to try every k value (including zero) and see which setting gives the most profit.

In other questions to implement dynamic programming(dp) we create a new array and make our additions-substractions on it. For this question we have to create a two dimensional array. One dimension represents the transactions and the other one represents the days. The costsarray is to store the price when we buy a stock. It is updated through the iteration (maximize because negative). In other words, we always try to buy at a minimum cost.

The coding part starts with reassigning these costs. Compare the buying cost with dp[i-1][j-1] - prices[i] where dp[i-1][j-1] is the maximum profit made from the previous j-1 transactions before making the current transaction. We update costs[j] as min(costs[j], dp[i-1][j-1] - prices[i]) so that costs[j] can keep track of the minimum cost, which is equivalent to the maximum total profit from the previous j-1 transactions and the cost of buying the stock on the ith day.

Current days profit at k = j, dp[i-1][j], is updated by comparing its value and the value it gets after the current transaction. Finally we return the maximum profit.

Time complexity: O(n^2) {nested loops}
Space complextiy: O(n^2) {2-D array}

"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        k = min(k, n // 2)
        dp = [[0] * (k + 1) for i in range(n)]
        costs = [-prices[0]] * (k + 1)

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i-1][j], prices[i] + costs[j])
                costs[j] = max(costs[j], dp[i-1][j-1] - prices[i])

        return max(max(dp))