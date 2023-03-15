from collections import Counter

def cutTheSticks(arr):
    result = []
    n = len(arr)
    x = Counter(arr)
    
    for i in sorted(x.keys()):
        result.append(n)
        n -= x[i]
        
    return result