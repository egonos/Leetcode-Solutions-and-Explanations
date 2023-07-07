"""
Intuition
Hi everybody! Today's problem can be solved via sliding window approach. I've used two pointers in this regard. In my first solution I assumed the the number of occurances can direct me in terms of defining the target element. The code I provide below works for mant cases but not all:
"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        left,right = 0,0
        n = len(answerKey)
        max_len = 0
        if answerKey.count('T') > n//2:
            target = 'T'

        else:
            target = 'F'

        while right<len(answerKey):
            if answerKey[right] == target:
                pass
            else:
                k-=1

            while k < 0:
                if answerKey[left] == target:
                    pass
                else:
                    k+=1

                left+=1

            max_len = max(max_len,right-left+1)
            right+=1

        return max_len

# I found the solution by trying each of the candidate (T & F), then return the maximum length from the trials.

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def helper(target,k):
            

            left,right = 0,0
            n = len(answerKey)
            max_len = 0
            

            while right<len(answerKey):
                if answerKey[right] == target:
                    pass
                else:
                    k-=1

                while k < 0:
                    if answerKey[left] == target:
                        pass
                    else:
                        k+=1

                    left+=1

                max_len = max(max_len,right-left+1)
                right+=1

            return max_len

        return max(helper('T',k),helper('F',k))
    
"""
Time complexity: O(n) {second loop is much shorther therefore not O(n^2)}
Space complexity: O(1)
"""