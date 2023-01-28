def hurdleRace(k, height):
    dose = 1
    if k > max(height):
        return 0
    elif k < max(height) or k == max(height):
        dose = max(height) - k
        return dose