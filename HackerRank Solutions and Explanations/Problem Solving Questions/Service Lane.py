"""
Explanation

The most important thing to note here is that the width is a global variable.
This initially confused me a lot.
All we are doing is slicing the width according the the start and end points and finding the minimum value in that slice.
"""

def serviceLane(n, cases):
    max_val = []
    for case in cases:
        start,end = case[0], case[1]
        corresponding = (width[start : end+1])
        max_val.append(min(corresponding))
        
    return max_val