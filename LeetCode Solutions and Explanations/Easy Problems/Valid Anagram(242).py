class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts = collections.Counter(s)
        tCounts = collections.Counter(t)
        return tCounts == sCounts
        