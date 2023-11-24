"""
Intuition
My code is not the most efficient yet it is really easy to understand. Basically for k times it pops the last index and inserts at the beginning of the array.
Time complexity: O(n*k)
Space complexity: O(1)

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0,nums.pop())
            k-=1