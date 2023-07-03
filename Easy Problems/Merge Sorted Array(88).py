"""
Intuition
To sort the values we can use .sort();
To merge two lists we can use slicing operations
[:m] -> relevant part of list1
Replace the [m:] part.

Complexity
Time complexity:
O((m+n) log (m+n))

Space complexity:
O(1)

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        nums1.sort()