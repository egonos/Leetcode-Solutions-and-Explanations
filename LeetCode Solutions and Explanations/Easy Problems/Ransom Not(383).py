class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineDict = collections.Counter(magazine)
        ransomNoteDict = collections.Counter(ransomNote)

        for ran in ransomNoteDict:
            if ran not in ransomNoteDict or magazineDict[ran] < ransomNoteDict[ran]:
                return False

        return True