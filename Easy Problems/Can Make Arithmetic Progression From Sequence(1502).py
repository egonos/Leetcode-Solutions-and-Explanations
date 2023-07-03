"""
Intuition
Hi everyone! This one is fairly straightforward. After sorting I used first difference as the referance and started a loop. If difference between two subsequent elements differ from this value the algorithm returns False. If it can loop till the end it returns True.

Time complexity: O(nlogn)
Space complexity: O(1)
"""

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        diff = arr[0]-arr[1]
        for i in range(len(arr)-1):
            c_diff = arr[i] - arr[i+1]
            if c_diff != diff:
                return False

        return True