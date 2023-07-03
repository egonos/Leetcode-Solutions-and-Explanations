"""
Approach
Two pointer approach

Complexity
Time complexity:
O(x/2) ~ O(x)
x-> length of the integer

Space complexity:
O(2) -> left and right characters
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x.startswith("-"): return False

        left,right = 0,len(x)-1
        while left<right:
            if x[left] == x[right]:
                left+=1
                right-=1

            else:
                return False

        return True
    

"""
Approach
Reverse the integer and see whether it remains the same.

Complexity
Time complexity:
O(log(x))

Space complexity:
O(log(x))
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False
