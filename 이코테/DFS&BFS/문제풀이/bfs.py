from collections import deque
def bfs(graph, start, visited):
	visited[start] = True
	queue = deque([start])
	while queue:
		compare = queue.popleft()
		print(compare, end = ' ')
		for v in graph[compare]:
			if visited[v] == False:
				visited[v] = True
				queue.append(v)


graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

