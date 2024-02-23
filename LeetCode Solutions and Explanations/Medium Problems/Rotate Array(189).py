class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        toLeft = nums[-rotate:]
        toRight = nums[:len(nums)-rotate]
        
        nums[:rotate],nums[rotate:] = toLeft,toRight