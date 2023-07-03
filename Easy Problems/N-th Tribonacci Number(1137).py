"""
Intuition
Hello everyone! For this problem, at first glance I've utilized recursion like when we are computing the Fibonacci numbers. However due to computational inefficiency of recursion it exceeded the time limit. You can find my initial solution in a comment form. After that I used the hint, and created an array. Each element of the array (expcept initial ones) are calculated based on the formula question provides. Hope you'll like it!
"""

class Solution:
    def tribonacci(self, n: int) -> int:

       # if n == 0: return 0
       # if n == 1: return 1
       # if n == 2: return 1
       # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 

       array = [0,1,1]
       for i in range(3,38): array.append(+array[i-1]+array[i-2]+array[i-3])

       return array[n]