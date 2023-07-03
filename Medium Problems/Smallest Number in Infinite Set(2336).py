"""
Intuition
Hi everyone! When I first read this question, I thought using a set() object is appropriate for this question due to lookup efficiency and I wrote something like this:
"""

class SmallestInfiniteSet:

    def __init__(self):
        
        self.global_set = set(range(1,1001))

    def popSmallest(self) -> int:
        #if not self.global_set: return
        min_num = min(self.global_set)
        self.global_set.remove(min_num)
        return min_num

        

    def addBack(self, num: int) -> None:
        self.global_set.add(num)

"""
It works succesfully however it performs poorly on time complexity (yet does not exceed the time limit). Therefore I've tried to solve this question by using queue and for the lookup I've used binary search.
"""

class SmallestInfiniteSet:
    def __init__(self):
        self.global_set = deque(range(1, 1001))

    def popSmallest(self) -> int:
        return self.global_set.popleft()

    def addBack(self, num: int) -> None:
        left, right = 0, len(self.global_set) - 1
        while left <= right:
            idx = (left + right) // 2
            mid = self.global_set[idx]
            if mid < num: left = idx + 1
            elif num < mid: right = idx - 1  
            else: return
                
        self.global_set.insert(left, num)

"""
This code basically do the same thing just uses binary search method to increase the lookup efficiency. Hope you like it!
"""