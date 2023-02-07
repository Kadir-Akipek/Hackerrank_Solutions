def findDigits(n):
    dividing = 0
    string = str(n)
    list_of_digits = []
    for i in string:
        list_of_digits.append(int(i))
    for i in list_of_digits:
        if i != 0 and n % i == 0:
            dividing += 1       
    return dividing
            