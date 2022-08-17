def DFS(v, visited, lst):
    visited[v] = 1
    if lst[v] == -1:
    	visited[v] = 2
    	return True
    if visited[lst[v]] == 0:
    	if not DFS(lst[v], visited, lst):
    		return False
    elif visited[lst[v]] == 1:
    	return False
    visited[v] = 2
    return True
class Solution:
    def canFinish(self, num: int, prerequisites: list) -> bool:
        visited = [0] * num
        lst = [-1] * num
        for elem in prerequisites:
        	lst[elem[0]] = elem[1]
        for i, elem in enumerate(visited):
        	if not elem:
        		if not DFS(i, visited, lst):
        			return False
        return True