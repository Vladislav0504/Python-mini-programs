def main():
    S = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in input():
        if char in brackets.values():
            S.append(char)
        elif not (S and brackets[char] == S.pop()):
            S.append(char)
            break
    if not S:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
