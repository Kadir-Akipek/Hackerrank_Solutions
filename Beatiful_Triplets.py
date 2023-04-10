def beautifulTriplets(d, arr):
    triplets = 0
    for i in arr:
        if i+d in arr and i+d*2 in arr:
            triplets += 1
            
    return triplets