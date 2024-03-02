
# O(log(n)) solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        return sorted(nums)

# O(n) solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        current = right

        result = [0]*len(nums)
        while left <= right:
            left_squared = nums[left]**2
            right_squared = nums[right]**2

            if right_squared >= left_squared:
                result[current] = right_squared
                right-=1

            else:
                result[current] = left_squared
                left+=1

            current -= 1

            

        return result