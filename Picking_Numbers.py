from collections import Counter

def pickingNumbers(a):
    arr = Counter(a)
    maxnumber = 0
    
    for i in range(99):
        maxnumber = max(maxnumber, arr[i] + arr[i+1])
        
    return maxnumber