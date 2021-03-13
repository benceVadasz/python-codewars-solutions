# my fastest solve ever

def delete_nth(order,max_e):
    fin = []
    for i in range(len(order)):
        if fin.count(order[i])<max_e:
            fin.append(order[i])
    return fin