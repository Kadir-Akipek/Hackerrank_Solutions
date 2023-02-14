def staircase(n):
    i = 1
    space = n - 1
    while (i <= n):
        print(" "*space + i*"#")
        i += 1
        space -= 1