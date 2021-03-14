def alphabet_position(text):
    l = list(text.lower())
    letters = [x for x in l if x.isalpha()]
    st=""
    for i in range(len(letters)):
        st+= str(ord(letters[i])-96)+" "
    return st[:-1]
