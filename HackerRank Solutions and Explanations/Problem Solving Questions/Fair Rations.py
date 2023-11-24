"""
For this problem, we have to adopt a greedy approach meaning that we have to compute till the end and check whether the output is appropriate.
For that purpose, we'll add one to each odd number and the number next to it then  check whether the last number is even or odd.
If it's odd, then we have failed so we'll print "NO". Otherwise, we'll print the number of addtions we have made.

"""

def fairRations(B):
    count = 0
    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i+1] +=1
            count +=2
    
    if B[-1] % 2 != 0:
        return "NO"
    
    else:
        return str(count)