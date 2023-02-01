def beautifulDays(i, j, k):
    count = 0
    
    for x in range(i,j+1):
        xreverse = int(str(x)[::-1])
        if abs(x - xreverse) % k == 0:
            count += 1
    return count