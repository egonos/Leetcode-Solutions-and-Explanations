class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            width = right - left
            area = max(area,min(height[left],height[right]) * width)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1

        return area
