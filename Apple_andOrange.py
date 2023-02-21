def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple,orange = 0,0
    x,y = 0,0
    for i in range(len(apples)):
        x = a + apples[i]
        if x >= s and x <= t:
            apple += 1
            
    for j in range(len(oranges)):
        y = b + oranges[j]
        if y >= s and y <= t:
            orange += 1
            
    print(apple)
    print(orange)