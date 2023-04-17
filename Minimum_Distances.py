def minimumDistances(a):
    result = []
    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                result.append(abs(i-j))
            
                
    if len(result) != 0:
        return min(result)
    else:
        return -1