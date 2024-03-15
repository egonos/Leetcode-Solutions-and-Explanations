class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n == 2:
            return 2

        solutions = [0] * n
        solutions[0] = 1
        solutions[1] = 2

        for i in range(2,n):
            solutions[i] = solutions[i-1] + solutions[i-2]

        return solutions[-1]
