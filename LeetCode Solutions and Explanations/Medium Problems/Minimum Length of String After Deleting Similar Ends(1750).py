class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            record = s[left]
            while left <= right and s[left] == record:
                left+=1

            while left <= right and s[right] == record:
                right -= 1

        
        if left > right:
            return 0

        else:
            return right - left + 1