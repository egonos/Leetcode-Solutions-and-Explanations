"""
Intuition
We have to define all the conditions:

The index is between start and end points (exclusive)
The index is at the starting point
The index is at the end point.
n is not equal to 1.
Adjacent places are empty.
Approach
Define this conditions as a conditional statement and see whether n becomes 0 eventually.

Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True

        pointer = 0
        while pointer < len(flowerbed):
             
            if pointer !=0 and pointer != len(flowerbed)-1 and flowerbed[pointer] == 0 and flowerbed[pointer-1] ==0 and flowerbed[pointer+1] == 0 :
                flowerbed[pointer] = 1
                n-=1

            elif pointer == 0 and flowerbed[pointer] == 0 and len(flowerbed)!= 1 and flowerbed[pointer+1] == 0:
                flowerbed[pointer] = 1
                n-=1

            elif pointer == len(flowerbed)-1 and flowerbed[pointer] == 0 and flowerbed[pointer-1] == 0:
                flowerbed[pointer] = 1
                n-=1

            else:
                pass

            if n == 0: return True
            pointer+=1

            