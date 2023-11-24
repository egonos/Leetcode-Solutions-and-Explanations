"""
Until obtaining the correct answer, the array is sorted in ascending order continuously basically...
"""

def countSwaps(a):
    count = 0
    i = 0
    a_sorted = sorted(a)
    while a != a_sorted:

        while i<len(a)-1:
            while i<len(a)-1 and a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                count+=1
            else:

                i+=1

        i = 0