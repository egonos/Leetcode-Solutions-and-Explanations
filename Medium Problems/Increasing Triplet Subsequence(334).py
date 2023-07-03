"""
Intuition
My intuition for this problem is to initiate two variables first and second to store the small and middle numbers. We have two conditions for replacement:

First has to be smaller than second
For both first and second the previous value should be bigger.
Approach
By using for loop we can guarantee that if we find such a sequence i<j<k condition also holds True.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for i in range(len(nums)):
            if nums[i] < first:
                first = nums[i]

            elif first < nums[i] < second:
                second = nums[i]


            else:
                pass

            if nums[i] > second > first:
                return True


        return False