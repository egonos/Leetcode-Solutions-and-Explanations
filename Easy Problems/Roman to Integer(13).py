"""
Intuition
If the second member of subsequent letter pairs is a bigger roman number then substract second from the first.

Directly add the number's value itself.

Approach
Create a dictionary to map integers and roman characters.

Complexity
Time complexity:
O(n)
n-> length of s

Space complexity:
O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        conv_dict = {}
        conv_dict["I"] = 1
        conv_dict["V"] = 5
        conv_dict["X"] = 10
        conv_dict["L"] = 50
        conv_dict["C"] = 100
        conv_dict["D"] = 500
        conv_dict["M"] = 1000

        sums = 0
        i = 0

        while i < len(s):
            
            if i+1 < len(s) and conv_dict[s[i]] < conv_dict[s[i+1]]:
                sums += conv_dict[s[i+1]] - conv_dict[s[i]]
                i+=2

            else:

                sums+= conv_dict[s[i]]

                i+=1


        return sums