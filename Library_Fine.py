def libraryFine(d1, m1, y1, d2, m2, y2):
    if m1 == m2 and y1 == y2:
        if d1-d2 <= 0:
            return 0
        else:
            return (d1-d2) * 15

    elif m1 != m2 and y1 == y2:
        if m1-m2 <= 0:
            return 0
        else:
            return (m1-m2) * 500
        
    if y1 != y2:
        if y1-y2 <= 0:
            return 0
        else:
            return (y1-y2) * 10000