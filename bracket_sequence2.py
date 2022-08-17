def main():
    S = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in input():
        if char in brackets.values():
            S.append(char)
        elif char in brackets and not (S and brackets[char] == S.pop()):
            S.append(char)
            break
    if not S:
        print('CORRECT')
    else:
        print('WRONG')


if __name__ == '__main__':
    main()
