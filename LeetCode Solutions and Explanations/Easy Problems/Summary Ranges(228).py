"""
Intuition
We can loop over the list and define two conditions

"a->b" if a != b
"a" if a == b

Then at the end we should include the last range.

Approach
for the indexing I've used pointer and looping I've used while. If pointer is equal to start index nums[start] is added to the return list. Otherwise when the arithmetic sequence is violated, nums[start]->nums[pointer-1] is added. At the last block we're handling the last range. We have to do it because we don't have any more numbers to compare the last range. Therefore we track it but not adding it.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)

"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        pointer = 1
        start = 0
        ret = []
        while pointer < len(nums):
            if nums[pointer] - nums[pointer-1] != 1:
                if start != pointer-1:
                    ret.append(str(nums[start]) + "->" + str(nums[pointer-1]))
                else:
                    ret.append(str(nums[start]))
                start = pointer
            pointer += 1

        # Handling the last range
        if start != pointer-1:
            ret.append(str(nums[start]) + "->" + str(nums[-1]))
        else:
            ret.append(str(nums[start]))

        return ret

