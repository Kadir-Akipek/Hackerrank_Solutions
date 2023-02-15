def miniMaxSum(arr):
    print(sum(arr)-max(arr),sum(arr)-min(arr))


#This is my solution but not supported 13TH case
"""def miniMaxSum(arr):
    resultmin = 0
    resultmax = 0
    for i in arr:
        if i < max(arr):
            resultmin += i
        if i > min(arr):
            resultmax += i
    
    print(resultmin,resultmax)"""