def repeatedString(s, n):
    liste = []
    total = len(s)
    over = True
    while total < n:
        for i in s:
            total += 1
            s += i

            if total == n:
                over = False
                break

    for i in s:
        liste.append(i)

    return liste.count("a")