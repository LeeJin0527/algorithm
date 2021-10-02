n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
for i in range(k):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

for i in graph:
	i = sorted(i)
# i
visited =[False] * (n+1)
def dfs(graph, v, visited):
	visited[v] = True
	# print(v, end =' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
dfs(graph, 1, visited)
cnt = 0
for i in visited:
	if i == True:
		cnt += 1
print(cnt-1)


