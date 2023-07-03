"""
Intuition
Hi everyone! For this problem, I've used binary search to find the optimal k. The initial value for left and right are 1 and maximum value at a given array respectively. Based on the time it takes to finish at a certain speed of k, left and right boundares are updated.

Approach
math.ceil() is a handy tool because it saves us to identify the different division conditions (modulo 0 and others)

Complexity
Time complexity:
-> Binary Search O(log n)
Space complexity:
-> O(1)

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        m = max(piles)
        if h == len(piles): return m
        left = 1 ; right = m ;
        while left<right:
            mid =  (left+right)//2

            total = 0
            for pile in piles:
                if pile <= mid: total+=1
                else: total += math.ceil(pile/mid)
                    

            
            if total >h: left = mid+1 
            else: right = mid
            


        return left

        