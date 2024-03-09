class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        max_length = 0
        common = set()
        while right < len(s):
            if not common or s[right] not in common:
                common.add(s[right])

                if right == len(s) - 1:
                    max_length = max(max_length,len(common))

            else:
                max_length = max(max_length,len(common))
                while s[right] in common:
                    
                    common.remove(s[left])
                    left+=1
                
                common.add(s[right])

            right+=1

        return max_length