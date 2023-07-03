"""
Intuition
Hello everyone! For this problem, first I applied the Brute Force approach. However it exceeded the time limit.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i]>max_profit: max_profit = prices[j]-prices[i]

        return max_profit
"""        
Therefore I tried different ways. The first way i tried is storing the prices with their indexes (as tuples), sorting and by using two pointers find the largest profit. It did not worked because when the maximum and minimum prices appear subsequently the algoritm gives wrong result. Here is the code version:
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        price_tuples = sorted([(price, idx) for idx, price in enumerate(prices)], key=lambda x: x[0], reverse=True)
        left, right = 0, n - 1

        def helper(left, right):
            if price_tuples[left][1] > price_tuples[right][1]:
                return price_tuples[right][0] - price_tuples[left][0]
            else:
                return 0

        while left < right:
            candidates = []
            if helper(left, right):
                return helper(left, right)

            if left + 1 < right and helper(left + 1, right): 
                candidates.append(helper(left + 1, right))
            if right - 1 > left and helper(left, right - 1): 
                candidates.append(helper(left, right - 1))

            if candidates:
                return max(candidates)

            left += 1
            right -= 1

        return 0
    
"""
Since it did not worked I continued my investigation and find this one eventually:
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(n):

            if prices[i] < min_price: min_price = prices[i]
            else: 
                if prices[i]- min_price > max_profit: max_profit = prices[i]- min_price


        return max_profit
"""
This one works and more efficient. Since we are usinf for the index issue was solved automatically. It stores the minimum indexed min price value then try to maximize the profit by comparing the differences with the max_profit. The time complexity is O(n) and space complexity is O(1). Note that brute force has O(n^2) time complexity (less efficient) and same space complexity. Hope you liked it.
"""