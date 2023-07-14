"""Intuition
Hi everybody. We need to solve this problem efficiently because otherwise it exceeds the time limit.

For example my initial solution,"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if difference == 0:
            return collections.Counter(arr).most_common(1)[0][1]
        sets = []
        for i in arr:
            if not sets:
                sets.append({i})
            else:
                for j in sets:
                    if i - difference in j:
                        j.add(i)
                        
                else:
                    sets.append({i})

        return max(len(i) for i in sets)
    
"""
is not valid due to this reason. Luckily, there is another way to solve this problem via dynamic programming. For example my final solution uses this method:
"""
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        storage = {}
        for i in arr:
            if i-difference not in storage:
                storage[i-difference] = 1

            else:
                pass

            storage[i] = storage[i-difference]+1

        return max(storage.values()) -1
"""              
1. Iterate over the array.
2. Check whether the number - difference in the storage dict.
3. If it's not add it to the dict and assign it's value to one.
4. At the end of each iteration assign the considered number's value as number - difference +1
5. To be honest, from my experiments the code always give the correct result + 1. That's why I'm substracting one in the end.

And that's it. I hope you'll find it useful.
"""