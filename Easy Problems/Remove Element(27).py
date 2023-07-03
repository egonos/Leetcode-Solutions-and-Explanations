"""
Intuition
The most important part of this problem is "inplace" adjustments. So it is appropriate to use .remove() method

Approach
As long as nums contain val, by using remove we delete it.

Complexity
Time complexity
O(n^2)
-> remove O(n)
-> shift O(n)

Space complexity
->O(1) only the removed element
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: nums.remove(val)
        return len(nums)
        