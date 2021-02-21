def find_in_array(seq, predicate): 
    for i in range(len(seq)):
        if predicate(seq[i], i):
            return i
    return -1