class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.strip().split()
        if len(pattern) != len(slist):
            return False
            
        items = set()
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if slist[i] not in items:
                    dic[pattern[i]] = slist[i]
                    items.add(slist[i])

                else:
                    return False

            else:
                if dic[pattern[i]] != slist[i]:
                    return False
        
        return True