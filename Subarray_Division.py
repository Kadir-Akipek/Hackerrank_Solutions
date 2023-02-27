def birthday(s, d, m):
    i = 0
    count = 0
    
    while m <= len(s):
        if sum(s[i:m]) == d:
            count += 1
        i += 1
        m += 1
    
    return count