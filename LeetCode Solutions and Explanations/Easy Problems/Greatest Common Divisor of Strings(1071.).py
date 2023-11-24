"""
Intuition
My intuition for this problem is to iterate through the shorter string and in each iteration check:

Whether it can form str1 when we stack a couple of them together.
Whether it can form str2 when we stack a couple of them togather.
Approach
To make sure that str2 is the shorter one, I assigned a conditional statement checking this. If not, then it replaces str1 and str2.
Start iteration in reverse and check the conditions I defined above. If it finds, then immediately end the loop because from there all we're doing is checking whether the conditions are applicable to the shorter strings.
Note that longest_candidate is initially empty for the nonexisting solutions. Whatever it takes at the end of the loop we return it's value.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): 
            str1, str2 = str2, str1
        longest_candidate = ""
        for i in range(len(str2), 0, -1):
            candidate = str2[:i]
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                    longest_candidate = candidate
                    break
        return longest_candidate

