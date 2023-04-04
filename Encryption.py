import math

def encryption(s):
    s = s.replace(" ","")
    l = len(s)
    rows = math.floor(math.sqrt(l))
    columns = math.ceil(math.sqrt(l))
    output = ""

    for i in range(columns):
        for j in range(i,l,columns):
            output+=s[j]
        output+=" "

    return output