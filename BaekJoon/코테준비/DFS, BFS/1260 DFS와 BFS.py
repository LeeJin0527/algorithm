from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfsVisited = [False] * (n+1)
bfsVisted = [False] * (n+1)
for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

for i in graph:
	i.sort()

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end= ' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
dfs(graph, v, dfsVisited)

def bfs(graph, start , visited):
	q = deque([start])
	visited[start] = True
	while q:
		v = q.popleft()
		print(v, end =' ')
		for i in graph[v]:
			if not visited[i]:
				q.append(i)
				visited[i]= True
print()
bfs(graph, v, bfsVisted)
