def solution(n):
    full, dec = str(n).split('.')
    if len(dec) <= 1:
        dec += '0'
    whole_num, deci_num = int(full), int(dec[0:2])
    if deci_num < 25:
        return whole_num
    elif 25 <= deci_num < 75:
        return whole_num + .5
    else:
        return whole_num + 1