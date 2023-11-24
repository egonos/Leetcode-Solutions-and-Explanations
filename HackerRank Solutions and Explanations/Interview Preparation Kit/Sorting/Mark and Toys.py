def maximumToys(prices, k):
    prices.sort()
    count = 0
    i = 0
    while k>0:
        count+=1
        k-=prices[i]
        i+=1
        
    return count-1