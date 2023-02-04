def saveThePrisoner(n, m, s):
    c = m % n
    if((c + s - 1) % n == 0): 
        return n
    else:
        return (c + s - 1) % n