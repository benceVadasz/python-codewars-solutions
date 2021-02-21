def title_case(title, minor_words=''):
    title_words = title.split(' ')
    if title == '':
        return ''
    if minor_words == '':
        return ' '.join([x.capitalize() for x in title_words])
    fin = ""
    low_words = minor_words.split(' ')
    lw = [x.lower() for x in low_words]

    for i in range(len(title_words)):
        if i == 0 or title_words[i].lower() not in lw:
            fin += title_words[i].lower().capitalize()
            fin += ' '
        else:
            fin += title_words[i].lower()
            fin += ' '

    return fin[:-1]


print(title_case('THE WIND IN THE WILLOWS', 'The In'))