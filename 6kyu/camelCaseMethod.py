def camel_case(string):
    spl = string.split(' ')
    bigs = [x.capitalize() for x in spl]
    return ''.join(bigs)