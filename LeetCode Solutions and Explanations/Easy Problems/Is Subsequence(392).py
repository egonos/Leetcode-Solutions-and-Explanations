"""
Intuition
My intuition for this problem is to store the t-indexes of letters found in s then check whether they are monotonically increasing.

Approach
To find the indexes, I've used find(). I've stored the relevant indexes in ix.

Complexity
Time complexity:
-> find(): O(n)
->while: O(n)
->for: O(n)

resulting: O(n^2)

Space complexity:
from index storing: O(n)

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        ix = []
       
        start = 0
        while pointer<len(s):
            candidate = s[pointer]
            idx = t.find(candidate,start)
            if idx == -1: return False

            else:
                ix.append(idx)
                pointer+=1
                start = idx+1

        for i in range(1,len(ix)):
            if ix[i-1] > ix[i]: return False


        return True