"""
Intuition
By using sliding window approach, we can effectively count the maximum occurances of vowels in a substring.

Approach
initial is the first substring and ret is the corresponding vowel count. current is used for counting the number of vowels in each window. If current is bigger than ret then we update the value of ret. On the other hand if ret is equal to the k, then there is no need to iterate so we immediately return the ret.

Complexity
Time complexity:
O(n)

Space complexity:
O(1)
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        initial = s[:k]
        vowels = set(['a', 'e', 'i', 'o','u'])
        ret = sum([initial.count(i) for i in vowels])
        current = ret
        if ret == k: return ret
        for i in range(k,len(s)):
            if s[i] in vowels and s[i-k] not in vowels:
                current+=1

            elif s[i] not in vowels and s[i-k] in vowels:
                current-=1

            else:
                pass

            
            ret = max(current,ret)
            if ret == k: return ret

        return ret