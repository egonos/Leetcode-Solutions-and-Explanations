"""
A problem is special if its index (within a chapter) is the same as the page number where it's located.
can iterate through each chapter and each problem within each chapter to check if iWe t's special.
Note: Got help from ChatGPT to understand the problem.
"""


def workbook(n, k, arr):
    page = 1
    count = 0
    for i in range(n):
        questions = arr[i]
        for q in range(1,questions+1): #indexing starts from 1; range excludes end pts
            if q == page: #question number is equal to the page number
                count +=1
                
            if q % k == 0 or q == arr[i]: #next page conditions
                page += 1
                
                
    return count