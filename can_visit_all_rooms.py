def DFS(v, visited, lst):
    visited[v] = True
    for w in lst[v]:
        if not visited[w]:
            DFS(w, visited, lst)
class Solution:
    def canVisitAllRooms(self, rooms: list) -> bool:
        visited = [False] * len(rooms)
        DFS(0, visited, rooms)
        if sum(visited) < len(rooms):
            return False
        return True