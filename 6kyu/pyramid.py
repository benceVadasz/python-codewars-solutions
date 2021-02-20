def pyramid(n):
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            arr[i].append(1)
    return arr
