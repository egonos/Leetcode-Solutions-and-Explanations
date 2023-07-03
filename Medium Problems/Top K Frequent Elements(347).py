"""
Intuition
To store the values and the corresponding frequencies, we can use hashmaps. Then by converting the hashmap into a list and returning the most frequent k ones, we can solve this problem

Approach
We can automatically create the frequency dictionary by using collections.Counter(). Then by using items() we can convert it into a list and sort them in descending order. Finally we can return the first k ones.

Complexity
Time complexity:
-> Sorting a list: O(log(n))

Space complexity:
O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_array = sorted(collections.Counter(nums).items(),key = lambda x: x[1], reverse = True)
        return [i for i,j in nums_array[:k]]
        