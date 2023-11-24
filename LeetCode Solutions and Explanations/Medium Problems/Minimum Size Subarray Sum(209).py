"""
Intuition
Hi everyone! Here is my solution for today's problem:
I adopted a sliding window approach by using two pointers (you can use for loops, it's just more convenint me to abstract when I use pointers instead). First I've defined the base case which is summation of nums is smaller than target. If that's the case there is no need to solve the problem. I've iterated through the array. When current_sum >= target I start another loop to shorten the tail of the subarray. As long as current_sum remains bigger than target, I've continued to shorten the subarray.

Time complexity: O(n) {second loop is much shorter}
Space complexity: O(1)

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
        if sum(nums) < target:
            return 0

        left = 0
        right = 0
        current_sum = 0
        min_length = float('inf')
        
        while right < len(nums):
            current_sum += nums[right]
            count = right-left+1
            
           # print(left, right, current_sum, min_length)
            while current_sum >= target:
                min_length = min(min_length, count)
                current_sum -= nums[left]
                count-=1
                left+=1
                
                    
            right+=1

        if min_length == float('inf'):
            return 0
        else:
            return min_length