n = int(input())
start, end = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(k):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def dfs(start):
	for i in graph[start]:
		if visited[i] == 0:
			visited[i] = visited[start]+1
			dfs(i)

dfs(start)
if visited[end] == 0:
	print(-1)
else:
	print(visited[end])