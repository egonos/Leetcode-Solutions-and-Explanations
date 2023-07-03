"""
Intuition
Hi everyone! For this problem the approach is fairly simple. Since we have not transaction fees, the total profit of many transactions is equal to the profit obtained from best entering and exiting point. Therefore we can follow a greedy approach.

The code has a time complexity of O(n) {from looping} and space complexity of O(1) since we are not storing the values in an array.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(1,len(prices)):
            profit =  prices[i]-prices[i-1]
            if  prices[i]-prices[i-1]>0: max_profit+= profit

        return max_profit