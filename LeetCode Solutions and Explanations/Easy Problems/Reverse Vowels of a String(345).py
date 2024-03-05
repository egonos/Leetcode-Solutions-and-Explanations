class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1 

        vowels = set(['a','e','i','o','u'])
        s_list = list(s)
        while left < right:

            while left < right and s_list[left].lower() not in vowels:
                left +=1

            while left < right and s_list[right].lower() not in vowels:
                right -= 1

            s_list[left],s_list[right] = s_list[right], s_list[left]

            left+=1
            right-=1

        return ''.join(s_list)

