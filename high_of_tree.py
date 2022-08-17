def main():
    n = int(input())
    tree = [[] for i in range(n + 1)]
    for i, vertex in enumerate(input().split()):
        tree[int(vertex)].append(i)
    h = 0
    stack = [tree[-1][0]]
    start, end = 0, 1
    while start < end:
        for i in range(start, end):
            stack.extend(tree[stack[i]])
        start, end = end, len(stack)
        h += 1
    print(h)


if __name__ == '__main__':
    main()
