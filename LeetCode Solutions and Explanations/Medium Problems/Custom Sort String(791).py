class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        letter_counts = {letter: 0 for letter in order}
        remainder = ""

        for letter in s:
            if letter in order:
                letter_counts[letter] = letter_counts.get(letter,0) + 1

            else:
                remainder += letter

        ordered_letters = ""
        for letter in order:
            ordered_letters += letter*letter_counts[letter]
        
        return ordered_letters + remainder