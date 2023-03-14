from collections import Counter

def sockmerchant(n,ar):
    narr = Counter(arr) 
    pair = 0 

    for i in range(max(ar)+1):
        while(narr[i] >= 2):
            pair += 2
            narr[i] -= 2

    return pair