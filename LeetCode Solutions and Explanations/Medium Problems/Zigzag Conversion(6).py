class Solution:
    def convert(self, s: str, numRows: int) -> str:


        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        pointer = 0
        forward = True

        for letter in s:
            rows[pointer].append(letter)

            if pointer == numRows - 1:
                forward = False

            elif pointer == 0:
                forward = True

            if forward:
                pointer+=1

            else:
                pointer -=1

        return ''.join(''.join(row) for row in rows)