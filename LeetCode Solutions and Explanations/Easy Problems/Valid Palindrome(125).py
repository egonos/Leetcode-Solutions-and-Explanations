class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerInput = s.lower()

        left = 0
        right = len(lowerInput) - 1

        while left <= right:
            while left<=right and not lowerInput[left].isalnum():
                left += 1

            while left <=right and not lowerInput[right].isalnum():
                right -= 1

            if left <= right and lowerInput[left] != lowerInput[right]:
                return False

            left+=1
            right-=1

        return True
