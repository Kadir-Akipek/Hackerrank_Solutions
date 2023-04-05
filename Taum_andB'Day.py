def taumBday(b, w, bc, wc, z):
    return min(b*bc + w*wc, b*bc + (bc+z)* w, w*wc + (wc+z)*b)