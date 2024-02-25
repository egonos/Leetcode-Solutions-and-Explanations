"""
Intuition
Hi everyone! For this problem, the most important thing in my opinion is to understand the logic behind prefix suffix multipication. Since we have a complexity boundary we can't use:

functools.reduce(): from my research, it has O(n) complexity; results in O(n^2) complexity for the whole code
Two cumulative multipication array with itertools.accumulate() or manually. Again results in O(n^2) complexity.
Lets dive into the math. When we calculate cumulative multipication in forward and backward pass then mutiply the resulting list elemetwise, we can obtain the solution. It's overwhelmed me a lot when I first learned it so if you feel like this please keep in mind that you're not the only one.

For example:
When we have this list [1,2,3,4]

right_accumulate = [1,1,1,1]
left_accumulate = [1,1,1,1]

when we update left_accumulate[i] based on the reult of multiplying left_accumulate[i-1] and nums[i-1], we get 1 (starting from 1st index; 1*1 = 1)
similarly,

i = 2
2*1 = 2
left_accumulate = [1,1,2,1]

i = 3
3*2 = 6
left_accumulate = [1,1,2,6]

We will do the same thing in reverse to the right_accumulate

i = 2
1*4 = 4
right_accumulate = [1,1,4,1]

i = 1
3*4 = 12
right_accumulate = [1,12,4,1]

i = 0
12*2 = 24
right_accumulate = [24,12,4,1]

when we multiply these elementwise, we get the solution:
[24,12,8,6]

This code has a time complexity of O(n) {from looping} and space complexity of O(n) {two arrays}. I hope this solution was helpful to the ones who got overwhelmed by math
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lefts,rights = [1]*len(nums),[1]* len(nums)
        for i in range(1,len(nums)):
            lefts[i] = lefts[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            rights[i] = rights[i+1] * nums[i+1]

        final = []
        for i in range(len(lefts)):
            final.append(lefts[i] * rights[i])

        return final
            