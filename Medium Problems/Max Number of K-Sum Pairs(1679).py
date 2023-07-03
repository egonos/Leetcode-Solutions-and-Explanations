"""
Intuition
Sorting and using two pointer approach is the easiest way to solve this problem (At least from my experience). Based on the magnitude op pair sums, the algorithm iteratively changes left and right pointer. If it finds a perfect pair then it increeases count by one.

Complexity
Time complexity:
->Sorting:O(nlogn)
->Looping: O(n)

Space complexity: O(1)
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        
        left,right = 0,len(nums)-1
        while left<right:
            temp = nums[left]+nums[right]
            if temp<k: left+=1
            elif temp>k:right-=1
            else: count+=1;left+=1;right-=1

        return count
