"""
Intuition
Hi everyone. Before showing my solution, I want to share my progresssion with you. In first glance, I've written something like this:
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]<= intervals[i+1][0]:
                pass

            else:
                count+=1

        return count
"""
The intention is good. Start with the minimum number in the array and control whether the ordered array overlaps or not. However this solution is not valid, because although the counting operation is correct, this algorithm does not capture which element to store when there is an overlap.

My second solution is this:

"""
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x: x[1])
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0]>=last_end:
                pass

            else:
                count += 1

        return count
"""
If I sort the array according to the values in the end I can decide which one to keep (The smaller one since it allows more room). However, this solution is also problematic because the last_endi is not updated during the iteration. All it's doing is comparing the smallest end value with the initial values. It is close but not enogh.

My final solution looks like this:

Code
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x: x[1])
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0]>=last_end:
                last_end = intervals[i][1]
                

            else:
                count += 1

        return count
"""      
When there is no overlap, the last_end is updated. The rest is the same.

The time complexity for this algoritm is O(n log n) {due to sorting}
The space complexity is O(1).
"""