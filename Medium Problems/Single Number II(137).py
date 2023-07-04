"""
Intuition
Hi everyone! For this problem I've used collections.Counter() to count number of occurances of each item. Then I've looped over the dict and have returned the variable if it's occurance count is not 3.

Time complexity: O(m+n) {counter object}
Space complexity: O(n) {count_dict}
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = collections.Counter(nums)

        for i,j in count_dict.items():
            if j != 3: return i