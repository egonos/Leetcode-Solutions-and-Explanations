"""
Intuition
Hi everyone! Today's question was challenging maybe just because I'm a novice at dp. I'm preparing this section to those who are having hard time to solve dp questions. Hope it would be helpful.

Now if the nums was sorted and we were trying to search arithmetic sequence in subsequent manner then the code like this would be enough:

"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) == 2: return 2
       # nums.sort()
        max_count = 2
        for i in range(len(nums)-1):
            count = 2
            dif = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == dif:
                    count += 1
                else:
                    break
            max_count = max(max_count, count)

        return max_count
"""
At least first I coded in that way. The real solution is a bit complex than this. We have to store the relative differences for each element in nums. To do that we need a dictionary for each element. In the code below it is called dp. Then we start a nested loop. i iterates through each number in nums and j is used for computing relative differences. If the calculated difference in our dict, we increase its count by one. and if not we assign the count as 2 (The smallest sequence) and add a new key having count of 2 to our dictionary. Finally we update the maximum length by comparing maximum length we've tracked so far with the count. The time complexity is O(n^2) {nested loop} and space complexity is also O(n^2) {store ~n variables for n elements.}
"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]  
        max_len = 2  
        
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]  
                if diff in dp[i]:
                    count = dp[i][diff] + 1
                else:
                    count = 2
                dp[j][diff] = count
                
                
                max_len = max(max_len, count)
                
        return max_len