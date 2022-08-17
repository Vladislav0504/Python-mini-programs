import sys
N = int(input())
T = {}
A = [-1] * (N + 1)
Nodes = {}
k = 0
for line in sys.stdin:
  if k < N - 1:
    x = int(line)
    A[k + 2] = x
    if x not in Nodes.keys():
      Nodes[x] = 1
    else:
      Nodes[x] += 1
    k += 1
  elif k == N - 1:
    for x in Nodes.keys():
      if Nodes[x] == 1:
        Nodes[x] = -1
    T[1] = [-1, 0]
    for i in range(2,N + 1):
      if Nodes[A[i]] > 0:
        T[i] = [A[i], Nodes[A[i]]]
        Nodes[A[i]] -= 1
      else:
        T[i] = [T[A[i]][0], T[A[i]][1]]
    k += 1
  else:
    x,y = map(int, line.split())
    if x == y:
      ans = x
    else:
      while x != y:
        if T[x][0] == T[y][0]:
          if T[x][1] == T[y][1]:
            ans = min(x,y)
            break
          else:
            ans = T[x][0]
            break
        else:
          if T[x][0] > T[y][0]:
            x = T[x][0]
          else:
            y = T[y][0]
        ans = x
    print(ans)