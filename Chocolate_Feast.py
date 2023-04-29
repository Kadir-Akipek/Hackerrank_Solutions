def chocolateFeast(n, c, m):
    chocolate = n // c
    wrapper = chocolate

    while(wrapper >= m):
        wrapper -= m
        chocolate += 1
        wrapper += 1
        
    return chocolate