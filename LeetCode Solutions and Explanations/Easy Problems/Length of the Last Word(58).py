class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char = len(s) - 1
        
        while 0 <= char and not s[char].isalnum():
            char -=1

        count = 0
        while 0 <= char and s[char].isalnum():
            count+=1
            char-=1

        return count