"""
Intuition
Hi everyone! For this problem first I've used a Brute Force however since it is not efficient, I've changed my approach and used stacks instad.
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [temp for temp in temperatures]
        n = len(ret)
        for i in range(n):
            pointer = i+1
            while pointer<n and ret[i] >= ret[pointer]:
                pointer+=1


            if pointer != n :
                ret[i] = pointer - i
            else:
                ret[i] = 0
           


        return ret

"""
Basically I've created a copy of the original temperatures array then check the first bigger number one step a time. Lastly I've updated my copy array accordingly. We are using nested loops so the time complexity would be O(n^2) and space complexity would be O(n) {the copy array}

The code below is my submisson code. In this algorithm, we append the i'th value of temperatures array then replace it with the index of the first occuring bigger number.


j = stack.pop()
ret[j] = i-j

Note that temperatures[stack[-1] refers the temperature which we are trying to find a biger one in the original array. The time complexity is O(n) {more efficient} and the space complexity is O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j = stack.pop()
                ret[j] = i-j

            else:
                stack.append(i)


        return ret