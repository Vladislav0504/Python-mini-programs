def main():
    S = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for n, char in enumerate(input(), 1):
        if char in brackets.values():
            S.append((char, n))
        elif char in brackets and not (S and brackets[char] == S.pop()[0]):
            S.append((char, n))
            break
    if not S:
        print('Success')
    else:
        print(S.pop()[1])


if __name__ == '__main__':
    main()
