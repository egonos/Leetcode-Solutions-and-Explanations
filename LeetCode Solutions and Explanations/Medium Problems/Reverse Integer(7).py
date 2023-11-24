"""
Intuition
To reverse the string, we can convert x into a string. If x is negative we can do the same thing starting from 1st index. At the end, we can add the 32 bit condition {-2**31<= x <= 2**31-1}

Approach
Use str() for string conversion.

Complexity
Time complexity: O(n) from traversing the digits
Space complexity: O(n) to store all the digits
Note: n refers to the number of digits.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:

            x_str = str(x)[1:]
            x_rev = "-" + x_str[::-1]

        else:
            x_str = str(x)
            x_rev = x_str[::-1]

        
        if -2**31<= int(x_rev) <= 2**31-1:
            return int(x_rev)

        else:
            return 0