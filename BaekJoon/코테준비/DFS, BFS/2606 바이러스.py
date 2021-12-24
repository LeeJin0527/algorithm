n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
for i in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

for i in range(n):
	graph[i].sort()


cnt = 0
def dfs(graph, v, visited):
	global cnt

	visited[v] = True
	for i in graph[v]:

		if not visited[i]:
			dfs(graph, i, visited)
			cnt += 1


dfs(graph, 1, visited)
print(cnt)