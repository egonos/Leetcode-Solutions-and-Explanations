"""
Intuition
Hi everyone! I'm currently working on dynamic programming and wanted to explain the solution so that I might reach people who are having a hard time learning it and I can be sure that I've also understood the concept. Hope it will be helpful to someone out there.

For this problem we have to follow a greedy approach among each jump. By trying each possibilities we should find the furthest distance and continue from there. Let's look at the code closely.

jumps is a variable to count the minimum number of jumps we need. Initial value is naturally 0. The current_jump_end is the pointer we use on the array to indicate our position after the last jump. It is also initially 0. furthest is used to compare the distances and store the biggest one. The loop goes through lenght of the array -1 because of the question statement. We iteratively compute the distance i + nums[i] and compare it with the maximum distance we encountered so far. When we reach the pointer; we increase the jump counts by one and update the position of the pointer accordingly. Finally we return the number of jumps. By using this method, we can guarantee that the number of jumps is actually equal to the minimum number of jumps because in each time we selected the option which carries us to the furtest. The time complexity is O(n) {from looping} and the space complexity is O(1) {since we don't save any array or something}.

An Example:
nums = [2,3,1,1,4]
current_jump_end = 0
furthest = 0
jumps = 0

1st iteration
current_jump_end = 2
furthest = 2
jumps = 1

2nd iteration
current_jump_end = {1,2}
furthest = {3+1 = 4; 2+1 = 3} -> select the first index which is 3
jumps = 2

return 2
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0 
        furthest = 0

        for i in range(len(nums)-1):
            if i + nums[i] > furthest: furthest = nums[i] +i
            if i == current_jump_end: jumps+=1; current_jump_end = furthest

        return jumps