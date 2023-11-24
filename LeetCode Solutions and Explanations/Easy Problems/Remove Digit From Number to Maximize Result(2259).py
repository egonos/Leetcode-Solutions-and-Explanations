"""
Intuition
In this problem, I tried the values and stored only the maximum one.

Approach
For iteration I've started a for loop. If the digit located at the given index is equal to the input digit, my algorithm concatenates the before and after part of the string. Then it converts it to an integer and compare with the maximum value {max_val} stored so far. At the end it returns the maximum value.

Complexity
Time complexity:
O(n) -> loop over the string

Space complexity:
O(n) -> max_value
"""

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_val = 0
        new = ""
        for i in range(len(number)):
            if number[i] == digit:
                new += number[:i]
                new += number[i+1:]
                if int(new) > max_val:
                    max_val = int(new)
                new = ""

                
                    
        
        return str(max_val)