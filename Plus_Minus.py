def plusMinus(arr):
    positive,negative,zero = 0,0,0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1

    print("{:.6f}".format(float(positive/len(arr))))
    print("{:.6f}".format(float(negative/len(arr))))
    print("{:.6f}".format(float(zero/len(arr))))