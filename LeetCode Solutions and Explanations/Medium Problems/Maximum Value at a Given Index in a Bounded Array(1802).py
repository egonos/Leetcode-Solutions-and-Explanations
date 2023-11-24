"""
Intuition
We have to make sure that all elements are positive.
We also have to make sure that we don't exceed maxSum.

A natural consequence of these two requirements are the following:

-> If candidate > left and/or right number of places decrease the elements by one as we pass. Ex: 2,3,4,3,2. So left outermost and right outermost values are mid - index

-> Maximum value for initial guess could be maxSum - n and the first mid guess is the average of maximum and 0.

By using binary search and applying these rules we can find the answer.

I hope this explaination is useful for the ones who struggle...
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calculate_min_sum(mid):
            """Calculates the minimum sum of the array for the given mid value"""
            
            
            if mid > index:
                left = mid - index
            else:
                left = 0

            left_sum = (mid + left) * (mid - left + 1) // 2

            if mid > n-1-index:
                right = mid - n + 1 + index

            else:
                right = 0

            
            right_sum = (mid + right) * (mid - right + 1) // 2 - mid
            
            return left_sum + right_sum <= maxSum

        res = 0
        maxSum -= n # the numbers have to be positive i.e. min numbers = 1
        # apply binary search
        low, high = 0, maxSum
        while low < high:
            mid = (low + high + 1) // 2

            if calculate_min_sum(mid):
                low = mid
            else:
                high = mid - 1

        return low + 1