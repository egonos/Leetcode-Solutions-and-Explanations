"""
Approach
Use for to create a loop and ord() for comparison

Complexity
Time complexity:
O(min(n,m))
n-> length of letters
m-> position of the answer.

Space complexity:
O(1) -> only the answer
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        target_ord = ord(target)
        for i in letters:
            if ord(i) > target_ord:

                return i


        return letters[0]


        