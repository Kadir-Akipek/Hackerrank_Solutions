def electronic_shop(keyboards,drives,b):
    cost = []
    for i in keyboards:
        for j in drives:
            if (i + j) <= b:
                c = i + j
                cost.append(c)
            else:
                pass
            
    if len(cost):           
        return max(cost)
    else:
        return -1
