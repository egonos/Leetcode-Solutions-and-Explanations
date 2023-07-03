"""
Intuition
Hi everyone! For the problems like these, using itertools module is very convenient. I used combinations() for this problem.
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        lst = list(range(1,10))
        return [result for result in itertools.combinations(lst,k) if sum(result) == n]