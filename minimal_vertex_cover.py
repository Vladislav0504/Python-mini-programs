import sys
def DFS(v, visited, edges, lst, lst2 = None):
  if not visited[v]:
    visited[v] = True
    if v in edges.keys():
      for child in edges[v]:
        if lst2 == None:
          if lst[child] == -1 or DFS(lst[child], visited, edges, lst):
            lst[child] = v
            return True
        else:
          lst2.add(child)
          DFS(lst[child], visited, edges, lst, lst2)
  return False
def main():
  with open('C:\\Users\\admin\\Downloads\\graph.txt', 'r') as f:
    reader = (tuple(map(int, line.split())) for line in f)#sys.stdin)
    v1, v2, e = next(reader)
    print(v1, v2, e)
    lst, lst2 = [-1] * (v1 + v2), set()
    edges = {}
    s1, s2 = set(), set()
    for el in reader:
      print(el[0], el[1])
      edges[el[0]] = edges.get(el[0], set()).union(set([el[1]]))
  visited = [False] * v1
  for i in range(v1):
    if DFS(i, visited, edges, lst):
      visited = [False] * v1
  for el in lst:
    if el != -1:
      s1.add(el)
  free_vertex1 = set(edges.keys()).difference(s1)
  if len(free_vertex1) == 0:
    print(*s1)
  else:
    visited = [False] * v1
    for el in free_vertex1:
      DFS(el, visited, edges, lst, lst2)
      visited = [False] * v1
    for el in lst2:
      s2.add(lst[el])
      print(el, end=' ')
    print(*set(edges.keys()).difference(free_vertex1.union(s2)))
if __name__ == '__main__':
  main()