from sys import stdin


def main():
    n_char, n_code = map(int, input().split())
    D = {}
    for i, line in enumerate(stdin):
        if i < n_char:
            char, code = line.strip().split(': ')
            D[code] = char
        else:
            st = line
    mystr = ''
    code = ''
    for el in st:
        code += el
        if code in D.keys():
            mystr += D[code]
            code = ''
    print(mystr)


if __name__ == '__main__':
    main()
