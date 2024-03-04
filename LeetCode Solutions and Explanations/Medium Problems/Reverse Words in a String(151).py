#1st Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.strip().split()
        return ' '.join(s_split[::-1])

#2nd Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.strip().split()
        left,right = 0,len(s_split)-1
        while left < right:
            s_split[left],s_split[right] = s_split[right], s_split[left]
            right-=1
            left+=1

        return ' '.join(s_split)