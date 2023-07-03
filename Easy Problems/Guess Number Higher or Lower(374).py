"""
Intuition
By using binary search, we can effectively find the solution we need.

Approach
We have two pointers left and right to update the final estimation. The update is based on the output of predefined function guess().

Complexity
Time complexity:
O(log n)
Space complexity:
O(1)

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left,right = 1,n
        
        while left< right:
            est = (left+right)//2
            if guess(est) == -1 : right = est-1
            elif guess(est) == 1: left = est+1
            else: return est
            
        return right 

        