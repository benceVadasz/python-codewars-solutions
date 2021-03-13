def spin_words(sentence):
    st = []
    spl = sentence.split(' ') if ' ' in sentence else [sentence]
    for i in range(len(spl)):
        if len(spl[i]) >= 5:
            st.append(spl[i][::-1])
        else:
            st.append(spl[i])
    return ' '.join(st)

print(spin_words('Hey fellow warriors'))