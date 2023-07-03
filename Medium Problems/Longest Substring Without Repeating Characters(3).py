"""
Approach
We can use two pointer approach in here. In each round we can calculate the window length and compare it with the maximum length observed so far.

Complexity
Time complexity:
O(n) coming from for loop

Space complexity:
O(min(n,m))
m -> length of the largest substring
n -> length of s
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        seen_chars = set()
        max_len = 0
        while right < len(s):
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                right+=1

            else:
                seen_chars.remove(s[left]) #remove immediately if the character is duplicated
                left+=1

            max_len = max(max_len, right - left)


        return max_len

            
