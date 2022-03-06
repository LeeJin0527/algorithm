n = int(input())
visited = [False] * (n+1)
graph = [[] * (n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
for i in graph:
	i.sort()
def dfs(x):

	visited[x] = True
	for i in graph[x]:
		if not visited[i]:
			visited[i] = True
			dfs(i)

dfs(1)
print(visited.count(1)-1)
