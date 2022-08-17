def DFS(v, visited, arr):
    visited[v] = True
    if arr[v] != 0:
        left, right = v - arr[v], v + arr[v]
        if right < len(arr) and not visited[right]:
            DFS(right, visited, arr)
        if left >= 0 and not visited[left]:
            DFS(left, visited, arr)
class Solution:
    def canReach(self, arr: list, start: int) -> bool:
        visited = [False] * len(arr)
        DFS(start, visited, arr)
        for i, elem in enumerate(arr):
            if elem == 0 and visited[i]:
                return True
        return False