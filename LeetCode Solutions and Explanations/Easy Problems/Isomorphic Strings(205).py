class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        items = set()
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] not in items:
                    items.add(t[i])
                    dic[s[i]] = t[i]
                else:
                    return False


            elif dic[s[i]] != t[i]:
                return False

        return True