

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_singular = sum([math.pow(i,2) for i in range(1,n+1)])
    sums = math.pow(sum([i for i in range(1,n+1)]),2)
    print(int(abs(sum_singular-sums)))