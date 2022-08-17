import sys
def TopSort(lst, deg, N):
  s = []
  Q = [v for v in range(N) if deg[v - 1] == 0]
  while Q:
    v = Q.pop(0)
    s.append(v)
    for u in lst[v - 1]:
      deg[u - 1] -= 1
      if deg[u - 1] == 0:
        Q.append(u)
  if len(s) == N:
    print(*s)
  else:
    print(-1)
def main():
  N, M = map(int, input().split())
  deg = [0] * N
  lst = [[] for i in range(N)]
  for line in sys.stdin:
    v1, v2 = map(int, line.split())
    if v2 not in lst[v1 - 1]:
      lst[v1 - 1].append(v2)
      deg[v2 - 1] += 1
  TopSort(lst, deg, N)
if __name__ == '__main__':
  main()