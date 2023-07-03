"""
Intuition
Due to inplace replacement requirement, I've used simultaneous adding and deleting operations in a loop

Approach
For the removal I89 used pop() and for the addition I've used append. .count() makes the algorithm resistant to non zero cases.

Complexity
Time complexity: O(n^2)
-> index: O(n)
-> count: O(n)
Space complexity:
-> O(1) changed variable
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    

        count = nums.count(0)
        for _ in range(count):
            zero_idx = nums.index(0)
            nums.append(nums.pop(zero_idx))
    

          
