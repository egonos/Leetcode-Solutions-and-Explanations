"""
Intuition
Hi everyone! For this question, I've also included my previous solutions since I think that they contain some valuable information. The first solution uses two for loops which exceeds the time limit. The second one is faster since when it encounters a successful potion*spell combo it automatically assigns the the number of successes as the number of potions - the first succesful index. But it still exceeds the time limit. The last solution on the other hand uses custom binary search method. Note that we append n-left instead of n-mid because mid does not necessarily be equal to the left. Free to try :) It gives error.

Complexity
Time complexity:
->Sorting O(nlog n)
->Loop O(n)
Resulting O(nlog n)

Space complexity:
-> ret list: O(n)

"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      #  ret = []
      #  for spell in spells: 
      #      candidates = [spell*potion for potion in potions]
      #      exceed = sum([int(candidate>=success) for candidate in candidates])
      #      ret.append(exceed)

       # return ret

# ------------------------------------

#        n = len(potions)
#        potions.sort()
#        ret = []
#        for spell in spells:

#            for i in range(n):
#                if potions[i]*spell >= success:
#                    ret.append((n-i))
#                    break

 #               else:
 #                   if i == n-1: ret.append(0)

 #                   else: pass

 #       return ret


        potions.sort()
        ret = []
        n = len(potions)
        for spell in spells:
            left,right = 0,n-1
            while left<=right:
                mid = (left+right)//2
                if potions[mid]*spell < success: left = mid+1
                else: right = mid-1

            ret.append(n-left)

        return ret