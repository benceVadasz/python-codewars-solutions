def high(x):
    l = x.split(' ')
    nu_l = []
    for i in range(len(l)):
        su = 0
        for j in range(len(l[i])):
            su += ord(l[i][j]) -96
        nu_l.append(su)
    max_ind = nu_l.index(max(nu_l))
    return l[max_ind]
