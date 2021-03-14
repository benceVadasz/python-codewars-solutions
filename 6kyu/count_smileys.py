def count_smileys(arr):
    fin = 0
    for i in range(len(arr)):
        if len(arr[i]) == 2:
            if (arr[i][0] == ':' or arr[i][0] == ';') and (arr[i][1] == ")" or arr[i][1] == 'D'):
                fin += 1
        elif len(arr[i]) == 3:
            if (arr[i][0] == ':' or arr[i][0] == ';') and (arr[i][1] == "-" or arr[i][1] == '~') and (
                    arr[i][2] == ")" or arr[i][2] == 'D'):
                fin += 1
