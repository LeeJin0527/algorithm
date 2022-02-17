import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
for i in graph:
	i.sort()


def dfs(v):
	visited[v] = True
	print(v, end = ' ')
	for i in graph[v]:
		if not visited[i]:
			visited[i] = True
			dfs(i)

def bfs():
	q = deque([v])
	visited[v] = True
	while q:
		x = q.popleft()
		print(x, end = ' ')
		for i in graph[x]:

			if not visited[i]:
				visited[i] = True
				q.append(i)
visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs()
