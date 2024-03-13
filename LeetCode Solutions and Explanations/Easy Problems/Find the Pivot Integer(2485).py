class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n == 1: return 1
        
        pivot = 1 
        leftSum = 1
        rightSum = sum(range(pivot,n+1))

        while leftSum < rightSum and pivot <=n:
            pivot+=1
            leftSum+=pivot
            rightSum -= pivot - 1
            if leftSum == rightSum:
                return pivot

        return -1