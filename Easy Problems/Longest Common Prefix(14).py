"""
Intuition
After defining the base conditions we can iteratively increase the length of the prefix and check it's validity by comparing across all the words.

Approach
``startswith()`-> To check the validity

while -> increase the length of the prefix

Complexity
Time complexity:
O(nm) -> m is the average length of the strings

Space complexity:
O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if "" in strs: return ""
        if len(strs) == 1: return strs[0]

        prefix = ""
        min_length = min([len(word) for word in strs])

        i = 0
        while i < min_length:
            candidate = strs[0][0:i+1]
            if all(word.startswith(candidate) for word in strs[1:]):
                i += 1
                prefix = candidate
            else:
                return prefix

        return prefix
