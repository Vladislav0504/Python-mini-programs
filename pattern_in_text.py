def h(s, p, x):
    k = 0
    for char in s[:0:-1]:
        k = (k + ord(char)) * x % p
    return (k + ord(s[0])) % p


def main():
    pattern = input()[::-1]
    text = input()[::-1]
    p, x = 1000000007, 263
    x_p = pow(x, len(pattern) - 1, p)
    delta = len(text) - len(pattern)
    h_text = h(text[delta:], p, x)
    h_pattern = h(pattern, p, x)
    for i in range(delta, -1, -1):
        if h_text == h_pattern and text[i:i + len(pattern)] == pattern:
            print(delta - i, end=' ')
        h_text = ((h_text - ord(text[i + len(pattern) - 1]) * x_p) * x + ord(text[i - 1])) % p


if __name__ == '__main__':
    main()
