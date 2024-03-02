class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        right = 0
        left = 0
        total = 0
        length = 99999999
        while right < len(nums):
            total += nums[right]
            while total >= target:
                length = min(length,right-left+1)
                total -= nums[left]
                left+=1

            
            right+=1

        return length