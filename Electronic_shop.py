b = 60
keyboards = [40,50,60]
drives = [5,8,12]

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


print(electronic_shop([40,50,60],[5,8,12],60))



"""b = 60
k = [40,50]
d = [5,8]

for i in k:
    for j in d:
        print(i + j)"""