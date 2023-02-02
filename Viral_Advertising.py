def viralAdvertising(n):
    shares = 5
    cumulative = 0
    for i in range(1,n+1):
        liked = int(shares/2)
        shares = liked * 3
        cumulative += liked
        
    return cumulative
