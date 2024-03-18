class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for i,num in enumerate(nums):
            if num not in positions:
                positions[num] = [i]
            
            else:
                positions[num].append(i)
                if positions[num][-1] - positions[num][-2] <= k:
                    return True

        return False