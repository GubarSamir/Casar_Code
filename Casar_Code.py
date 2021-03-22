def caesar(stringer):
    string = stringer.split()
    out_str = ''
    for i in string:
        for j in i:
            if j.isalpha():
                out_str += sdvig(j, count_char(i))
            else:
                out_str += j
        out_str += ' '
    return out_str[:-1]


def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()


def count_char(x):
    s = x.replace('"', '').replace(',', '').replace('!', '').replace('.', '')
    return len(s)


text = input()
print(caesar(text))
