def namelist(names):
    fin = ""
    for i in range(len(names)):
        if i + 2 < len(names):
            fin += names[i]['name'] + ', '
        elif i + 2 == len(names):
            fin += names[i]['name'] + " & "
        else:
            fin += names[i]['name']
    return fin

