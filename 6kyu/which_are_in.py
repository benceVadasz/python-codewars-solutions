def in_array(a1, a2):
    fin = []
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i] in a2[j] and a1[i] not in fin:
                fin.append(a1[i])

    return sorted(fin)