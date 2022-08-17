def knapsack_without_reps(W, w, n):
  	D = [[0 for i in range(n + 1)] for m in range(W + 1)]
  	for i in range(1, n + 1):
        for m in range(1, W + 1):
            D[m][i] = D[m][i - 1]
            if w[i - 1] <= m:
                D[m][i] = max(D[m][i], D[m - w[i - 1]][i - 1] + w[i - 1])
  	return D[W][n]


def main():
    W, n = map(int, input().split())
    w = [int(m) for m in input().split()]
    print(knapsack_without_reps(W, w, n))


if __name__ == '__main__':
    main()
