"""
Intuition
We can create two storage units (lists,sets, dicts etc.) to store the rows and columns separetely. Then we can compare them. While I was solving this problem, I've first used sets since they are very efficient in lookup operations (.intersection()). However, it is not possible to store duplites in a set so I used lists instead. While seaching through the lists it is important to consider the duplicates. Because of that len(row[i] for i in range (len(rows) if rows[i] in cols)]) like codes does not work properly. Using .count() is better instead.

Approach
pointer is the column index indicator. Using it with a for loop gives us an ooportunity to store the columns. Storing rows is more straightforward. Just loop over the grid and that's it.

Complexity
- Time complexity: It is O(n^2) where n is the size of the grid. {O(n) for iterating for the rows and O(n) for iterating over columns}

- Space complexity: It is also O(n^2). {O(n) for storing the rows and O(n) for storing the columns}
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        for r in range(len(grid)):
            row = grid[r]
            rows.append(row)

        pointer = 0



        while pointer < len(grid):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][pointer])

            pointer+=1
            cols.append(col)


        counts = 0
        for i in range(len(rows)):
            counts+= cols.count(rows[i])
        
        return counts

        
            
           
            