def divisibleSumPairs(n, k, ar):
    pair = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                pair += 1

    return pair