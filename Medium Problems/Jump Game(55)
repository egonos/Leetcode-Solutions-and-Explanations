"""
Intuition
Hi everyone. This problem is a dynamic programming question and I'm really having hard time to understand the logic behind this topic. I know I'm not alone and rhat's why I've perpared this section. Hope it will be helpful.

Now, our first goal is to solve the problem but besides that we want to solve the question as efficient as we could. Solving with forward pass is possible yet not efficient. It is a greedy approach therefore we need to check every possible scenarios to decide. On the other hand, iterating backwards is efficient. All we need to do is:

Define a target index
See whether we can reach there from previous index
If its possible then update the target to the previous index.
In the end, if we are in the beginning then yes we can reach to the end from the start. If not the opposite is true.
Initially the target is the last index. We start iterating backwards. idx+nums[idx] has to be at least equal to the target. For example:

idx = 3
target = 4
nums[idx] = 1

Then I can reach the target from index 3. Therefore I should update my target to 3.

And thats it! This solution has O(n) time complexity {from looping} and O(1) space complexity {store only the target}

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        for idx in range(n-1,-1,-1):
            if idx + nums[idx] >= target:
                target = idx

        return target == 0