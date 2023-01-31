def angryProfessor(k, a):
    threshold = 0
    time = 0
    left = 0

    for i in range(len(a)):
        if a[i] > time:
            left += 1
        else:
            pass
    threshold = n - left
    if threshold >= k:
        return "NO"
    else:
        return "YES"
