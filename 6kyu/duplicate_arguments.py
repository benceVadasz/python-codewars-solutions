def solution(*args):
    lst = []
    for i in range(len(args)):
        if args[i] not in lst:
            lst.append(args[i])
        else:
            return True
    return False
# return len(args) != len(set(args))

