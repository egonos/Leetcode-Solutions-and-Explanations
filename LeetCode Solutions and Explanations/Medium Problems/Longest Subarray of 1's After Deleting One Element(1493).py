"""
Intuition
Hi everybody! To be honest, todays problem have challenged me a bit. Here is my journey:

After trying on many examples this code arised:
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        try:
            while nums[start] == 0: start+=1
        except:
            return 0
        
        zero = False
        count = 0
        max_count = 0
        for num in nums[start:]:
            print("num:",num)
            if num == 1: count+=1;  max_count = max(count, max_count)
            elif num == 0 and not zero: zero = True
            else: count = 0; zero = False
            print(count, max_count,zero)
            print()

        if max_count == len(nums): return max_count-1
        else: return max_count
"""
It basically starts from first nonzero element and counts the number of ones giving one zero permission. However it is not fully working. It's only considering the first longest one array which is 7


a.longestSubarray([1,0,1,1,1,1,1,1,0,1,1,1,1,1])
Output = 7


Then I erased all of them and start from the begining. This time I've used two pointers. Both of them initially starts from 0'th index. Right one does the main traversion and if it encounters 1, it increases zeroby one. At the same time left acts as a place holder. When it encounters zero and zero count is more than one, it skips the current index.

Time complexity: O(n) {from looping}
Space Complexity: O(1)

"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right = 0,0
        zero = 0
        max_len = 0
        while right < len(nums):
            if nums[right] == 0: zero+=1
            while zero>1:
                if nums[left] == 0: 
                    zero -=1
                
                left+=1
            max_len = max(max_len,right-left)
            right+=1

        return max_len