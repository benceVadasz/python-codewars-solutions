from functools import reduce


def persistence(n):
    s = str(n)
    res = 0
    while len(s) > 1:
        spl = list(s)
        digits = [int(s) for s in spl]
        m = reduce(lambda x, y: x * y, digits)
        s = str(m)
        res+=1
    return res


print(persistence(39))