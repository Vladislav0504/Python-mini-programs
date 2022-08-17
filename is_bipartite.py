def DFS(v, visited, lst, color):
    visited[v] = color
    for w in lst[v]:
    	if visited[w] == 0:
    		DFS(w, visited, lst, -color)
def Bichromatic(graph, visited):
	for i, v in enumerate(graph):
		for el in v:
			if visited[i] == visited[el]:
				return False
	return True
class Solution:
    def isBipartite(self, graph: list) -> bool:
        visited = [0] * len(graph)
        for i, elem in enumerate(visited):
        	if not elem:
        		DFS(i, visited, graph, 1)
        return Bichromatic(graph, visited)