def tower_builder(n_floors):
    l = []
    for i in range(n_floors):
        diff = n_floors-i-1
        l.append(diff*' ' + ((i+1)*2-1) * '*'+ diff*' ')
    return l