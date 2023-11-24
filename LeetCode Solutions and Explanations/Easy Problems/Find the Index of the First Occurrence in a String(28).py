"""
Intuition
Hi everyone! The question statement exacty describes the dunction of .find(). By using this method we can solve the question effortless.
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)