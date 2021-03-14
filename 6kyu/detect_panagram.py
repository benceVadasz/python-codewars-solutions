import string

def is_pangram(s):
    pangram = "The quick, brown fox jumps over the lazy dog!"
    to_check = list(s.strip())
    p = sorted([ord(x.lower()) for x in pangram.strip()])
    t = sorted([ord(x.lower()) for x in to_check])
    for i in range(len(t)):
        if p[i] != t[i] and i<27:
            return False
    return True


print(is_pangram('Pack my box with five dozen liquor jugs.'))