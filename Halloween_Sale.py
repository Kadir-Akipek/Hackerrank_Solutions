def howManyGames(p, d, m, s):
    cost = 0
    cost += p
    count = 0
    
    while s >= cost:
        if m >= (p-d):
            cost += m
            count += 1
        else:
            p -= d
            cost += p
            count += 1
            
    return count

print(howManyGames(20,3,6,85))