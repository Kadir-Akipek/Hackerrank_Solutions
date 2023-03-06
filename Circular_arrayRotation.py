def circularArrayRotation(a, k, queries):
    newlist = []
    for i in range(k):
        n = a[len(a)-1]
        a.insert(0, n)
        a.pop()
        
    for i in range(len(queries)):
        b = queries[i]
        newlist.append(a[b])
    
    return newlist