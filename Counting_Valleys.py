def countingValleys(steps, path):
    sealevel = 0
    valley = 0
    for i in path:
        if i == "D":
            sealevel -= 1
        else:
            sealevel += 1
            if sealevel == 0:
                valley += 1
    return valley
