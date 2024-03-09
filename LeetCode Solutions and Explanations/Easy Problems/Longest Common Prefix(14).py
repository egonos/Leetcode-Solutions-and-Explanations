class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        pointer = 0
        common = ""
        try: 
            while True:
                current_common = ""
                for st in strs:
                    if not current_common:
                        current_common += st[pointer]
                        
                    elif current_common[-1] != st[pointer]:
                        return common

                    
                common += current_common
                pointer+=1

        except:
            return common
