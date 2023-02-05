def utopianTree(n):
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += 1
        else:
            total *= 2
    return total