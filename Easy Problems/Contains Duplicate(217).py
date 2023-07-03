"""
Intuition
To maximize the efficiency,

Use Hashmaps
Stop iteration immediately if a duplicate is detected
Approach
Create a dict to store and search through the elements. Return Trueimmediately when a duplication is detected

Complexity
Time complexity:
O(n)

Space complexity:
O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                
                return True
            else:
                nums_dict[i] = 1

        return False
    
"""
Intuition
Hash sets can only store the distinct values. We can use this.

Approach
Check whether the length of the list is equal to the hash set of the list

Complexity
Time complexity:
O(n)

n-> Length of the list

Space complexity:
O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))