def iq_test(numbers):
    odds = []
    evens = []
    lst = numbers.split(" ")
    for i in range(len(lst)):
        if int(lst[i]) % 2 == 1:
            odds.append(lst[i])
        else:
            evens.append(lst[i])
    if len(odds) == 1:
        return lst.index(odds[0]) + 1
    else:
        return lst.index(evens[0]) + 1


print(iq_test("2 4 7 8 10"))