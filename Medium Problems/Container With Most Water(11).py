"""
Intuition
My intuition is to iteratively calculate the area and compare it with maximum area calculated so far. If left side is shorter then left pointer moves to the right, if otherwise right pointer moves to the left.

Approach
Start a while loop. In each iteration, calculate the width and based on this and minumum height calculate the area. Compare it with max_area and update it accordingly.

Complexity
Time complexity:
-> loop: O(n)

Space complexity:
-> O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        

        max_area = 0

        while left < right:
            width = right-left
            if height[left] < height[right]:
                area = height[left]*width
                if area > max_area:
                    max_area = area
                left+=1

            else:
                area = height[right]*width
                if area > max_area:
                    max_area = area

                right-=1

        
        return max_area
