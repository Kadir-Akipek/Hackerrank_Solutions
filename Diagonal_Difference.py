def diagonalDifference(arr):
    firstnumber,secondnumber = 0,0
    x = 0
    y = len(arr) - 1
    while 1 != 0:
        firstnumber += arr[x][x]
        secondnumber += arr[x][y]
        x += 1
        y -= 1
        if x == len(arr):
            break    

    return abs(firstnumber - secondnumber)