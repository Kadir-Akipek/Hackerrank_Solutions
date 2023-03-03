x = 2
y = 5
z = 4

def catAndMouse(x,y,z):
    cat1 = abs(x-z)
    cat2 = abs(y-z)

    if cat1 == cat2:
        return "Mouse C"
    elif cat1 < cat2:
        return "Cat A"
    else:
        return "Cat B"

catAndMouse(2,5,4)
