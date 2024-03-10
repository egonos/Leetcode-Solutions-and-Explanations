class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s: return True
        pointer = 0

        for idx in t:
            if pointer == len(s) - 1 and s[pointer] == idx:
                return True

            if s[pointer] == idx:
                pointer +=1
            
        return False