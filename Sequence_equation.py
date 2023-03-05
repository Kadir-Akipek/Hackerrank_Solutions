def permutationEquation(p):
    newlist = []
    for x in range(1, len(p)+1):
        a = p.index(x) + 1
        newlist.append(p.index(a) + 1)
            
    return newlist