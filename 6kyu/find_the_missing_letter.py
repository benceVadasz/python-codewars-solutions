def find_missing_letter(chars):
    digits = [ord(x) for x in chars]
    for i in range(len(digits) - 1):
        if digits[i] + 1 != digits[i + 1]:
            return chr(digits[i]+1)



print(find_missing_letter(['a','b','c','d','f']))