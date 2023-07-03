"""
Intuition
For this problem, in my first attempt, I've utilized Counter() object for find the majority element:
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)
        limit = len(nums)/2
        
        for i,j in counter.items(): 
            if j>limit: return i

"""
Then to improve the efficiency I constructed the count dictionary from scratch. The mian difference between the two is second one immediately stops when it finds the mojority element whereas the first one completes its job then looks up the majority element. The time complexity is O(n) and the space complexity is also O(n).
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_dict = {}
        limit = len(nums)/2
        for num in nums:
            if num not in count_dict: count_dict[num] = 1
            else: 
                count_dict[num]+=1
            if count_dict[num] > limit: return num