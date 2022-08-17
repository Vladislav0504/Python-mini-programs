import sys
for ln in sys.stdin:
    n, s = '', ''
    ind = 0
    for i in range(len(ln)):
        if ind == 0 and ln[i] != '$':
            s += ln[i]
        elif ln[i] == '$':
            ind = 1
        else:
            n += ln[i]
            if i == len(ln) - 1 or not ln[i + 1].isdigit():
                ind = 0
                n = int(n) * 75
                n = '{:,}'.format(n).replace(',', ' ') + 'р'
                s += n
    sys.stdout.write(s)
