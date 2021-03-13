def create_phone_number(n):
    strings = [str(nu) for nu in n]
    res = ""
    for i in range(len(strings)):
        if i == 0:
            res += "(" + strings[i]
        elif i == 2:
            res += strings[i] + ") "
        elif i == 5:
            res += strings[i] + "-"
        else:
            res += strings[i]

    return res