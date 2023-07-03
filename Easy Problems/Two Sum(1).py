"""
Intuition
Instead of trying all the combinations in a nested loop, I calculated the complementary variables and find their index if they are in the array. If it is and the two index are not equal then I returned them

Approach
The complementary variable doesn't have to be in the array. To handle this, I've used try-except statements. Besides handling the error,except statement allowed me to pass the index comparison part also.

Complexity
Time complexity:
O(n^2)
->from index()
->from loop

Space complexity:
O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx1 in range(len(nums)):
            complementary = target - nums[idx1]
            try:
                idx2 = nums.index(complementary)

            except:
                continue

            if idx1 != idx2:
                return idx1,idx2