def migratoryBirds(arr):
    newlist = [0] * len(arr) 
    for i in range(len(arr)):
        newlist[arr[i]] += 1
    
    return newlist.index(max(newlist))
