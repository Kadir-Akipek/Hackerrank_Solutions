def compareTriplets(a, b):
    alicescore = 0
    bobscore = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alicescore += 1
        elif b[i] > a[i]:
            bobscore += 1
    return alicescore,bobscore