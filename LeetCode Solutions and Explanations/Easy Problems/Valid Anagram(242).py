"""
Intuition
We can create a hash map for each and compare them

Approach
Using collections.Counter() is the easiest way to create the hashmap we need.

Complexity
Time complexity:
O(log(n))

Space complexity:
O(log(n))
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)

        return sorted(t_dict.items())==sorted(s_dict.items())