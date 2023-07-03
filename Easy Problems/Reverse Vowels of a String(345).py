"""
Intuition
By using two pointers, we can detect the vovels both left and right side of the string and replace them.

Approach
Using sets is better for this problem due to its search efficiency.
Converting string to a list is crucial since the strings are immutable objects.
Since string operations are computationally expensive, including only one list to string conversion (at the final) is better.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set(["a","e","i","o","u","A","E","I","O","U"])

        s_list = list(s)

        left,right = 0,len(s)-1

        while left < right:

            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left+=1
                right-=1

            if s_list[left] not in vowels:
                left+=1

            if s_list[right] not in vowels:
                right-=1

        return ''.join(s_list)
