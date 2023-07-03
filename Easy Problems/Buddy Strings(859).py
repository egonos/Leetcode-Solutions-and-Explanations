"""
Intuition
Hi everyone! My code do the following:

Check whether two strings have the same length: If it's not returns False.
Checks whether the difference between two is more than two: If thats's the case it returns False.
Applies a different procedure to the special cases:
"aa" (return len(set(s)) < len(s))

"ab","ba" (return sorted(s) == sorted(goal)
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): 
            return False
        count = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                if count > 2:
                    return False
        if count == 0:
            return len(set(s)) < len(s)
        
        return sorted(s) == sorted(goal)