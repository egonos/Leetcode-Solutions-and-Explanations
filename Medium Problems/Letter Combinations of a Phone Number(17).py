"""
Intuition
Hello everyone. This is my solution. For this question, the main hero is itertools.product(). It gives exactly the output we need. The other parts are only for mapping and preparing the input for that function.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if digits == "":  return

        digit_list = [map_dict[digit] for digit in digits]
        return [''.join(comb) for comb in itertools.product(*digit_list)]