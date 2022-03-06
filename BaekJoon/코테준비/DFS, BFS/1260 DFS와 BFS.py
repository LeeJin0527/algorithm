from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
for i in graph:
	i.sort()

dvisited = [False] * (n+1)
def dfs(graph, start, visited):
	visited[start] = True
	print(start, end = ' ')
	for i in graph[start]:
		if not visited[i]:
			visited[i] = True
			dfs(graph, i, visited)


bvisited = [False] * (n+1)
def bfs(graph, start, visited):
	q = deque()
	q.append(start)
	while q:
		x = q.popleft()
		print(x, end = ' ')
		visited[x] = True
		for i in graph[x]:
			if not visited[i]:
				visited[i] = True
				q.append(i)
dfs(graph, v, dvisited)
print()
bfs(graph, v, bvisited)