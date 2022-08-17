n = int(input())
A = [[1 for i in range(n)] for j in range(n)]
y, x = (n - 1) // 2, (n - 1) // 2
action = {0: [1, 0, 0], 1: [0, 1, 1], 2: [-1, 0, 0], 3: [0, -1, 1]}
c, k = 1, 1
for j in range(2 * n - 1):
    for i in range(c):
        A[y][x] = (' ') * (len(str(n ** 2)) - len(str(k))) + str(k)
        x += action[j % 4][0]
        y += action[j % 4][1]
        k += 1
    c += action[j % 4][2]
for i in range(n):
    print(*A[i])
