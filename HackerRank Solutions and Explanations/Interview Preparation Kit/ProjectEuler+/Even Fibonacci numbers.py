"""
Inefficient Solution (Using Recursive Functions)
"""
def fibo_generator(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_generator(n-2) + fibo_generator(n-1)
        
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    m = 1
    fibo_list = set()
    while fibo_generator(m)< n:
        if fibo_generator(m) %2 == 0:
            
            fibo_list.add(fibo_generator(m))
            
        m+=1
        
    print(sum(fibo_list))


    """
    Efficient Solution (Using Iterative Function)
    """


def fibo_generator(n):
    fibo_list = [0,1]
    while fibo_list[-1]<n:
        fibo_list.append(fibo_list[-1]+fibo_list[-2])
        
    return sum([x for x in fibo_list if x%2 == 0 and x < n])
        
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibo_generator(n))
    