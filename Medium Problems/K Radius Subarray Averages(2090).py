"""
Intuition
Hi everyone! This question was really annoying and took my long time. In each of my trial just a small error occured which made me crazy. I'll provide two working answers with you. First one, as always exceeded the time limit so I implemeted the sliding window approach. Here is the first one:
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        return_array = []
        n = len(nums)

        for i in range(n):
            if i - k >= 0 and i+k+1 <= n:
                return_array.append(sum(nums[i-k:i+k+1])//(2*k+1))

            else:
                return_array.append(-1)

        return return_array
    
"""
It basically adds -1's in the front and the back side of the array then fill the middle according to the instractions. Instead of calculating the sum from stratch each time we can add the new added value to the previous sum and substract the removed value. When I used empthy list and add one by one in each iteration like I did in the brute force approach, most of the cases work perfectly but when k = 7875 it gives an output of 7876. I'll provide a not working solution with you:
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        return_array = []
        n = len(nums)
        i = 0
        if n<k:
            return [-1]*n

        while i-k<0:
            return_array.append(-1)
            i+=1
    

        idx = i
        current_sum = sum(nums[idx-k:idx+k+1])
        return_array.append(current_sum//(2*k+1))
        while idx+k+1 < n:
            current_sum = current_sum + nums[idx+k+1] - nums[idx-k]
            return_array.append(current_sum//(2*k+1))
            idx+=1

        while len(return_array)<n:
            return_array.append(-1)


        return return_array
    

"""          
From there after trying lots of different things, I solved like this:
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        return_array = [-1]*n

        if n < 2*k+1:  
            return return_array

        idx = k
        current_sum = sum(nums[idx-k:idx+k+1])
        return_array[idx] = current_sum//(2*k+1)
        idx += 1

        while idx + k < n: 
            current_sum = current_sum - nums[idx-k-1] + nums[idx+k]  
            return_array[idx] = current_sum//(2*k+1)
            idx += 1

        return return_array
    
"""
Instead of appending one by one, I initialized an array having equal length with the original array. The array only consists -1 values initially. The the algorithm handles the middle values according to the instuctions. Hope that is helpful for everyone!

Time Complexity: O(n) {from looping}
Space Complexity: O(n) {the return_array}
"""
