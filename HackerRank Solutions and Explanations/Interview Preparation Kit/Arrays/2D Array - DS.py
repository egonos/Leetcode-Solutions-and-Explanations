def hourglassSum(arr):
    col = 0
    row = 1
    max_ = float('-inf')
    for row in range(1,5):
        
        while col < 4:
            max_ = max(max_,sum(arr[row-1][col:col+3]) + arr[row][col+1] + sum(arr[row+1][col:col+3]))
            col+=1
        else:
            col = 0
            
    return max_