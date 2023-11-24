"""
Intuition
Using sliding window approach to maximize the efficiency.
Time complexity: O(n)
Space complexity: O(1)

"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
 #       max_array = deque(nums[:k])
 #       max_sum = sum(max_array)

 #       for i in range(k,len(nums)):
 #           max_array.append(nums[i])
 #           max_array.popleft()
 #           max_sum = max(max_sum,sum(max_array))

 #       return max_sum/k


            max_array = nums[:k]
            max_sum = sum(max_array)
            current_sum = max_sum

            for i in range(k,len(nums)):
                current_sum = current_sum+nums[i] - nums[i-k]
                max_sum = max(max_sum,current_sum)

            return max_sum/k