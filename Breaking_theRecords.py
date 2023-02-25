def breakingRecords(scores):
    mini,maxi = scores[0],scores[0]
    minbreak,maxbreak= 0,0
    for i in range(len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
            maxbreak += 1
        if scores[i] < mini:
            mini = scores[i]
            minbreak += 1
        
    return [maxbreak,minbreak]