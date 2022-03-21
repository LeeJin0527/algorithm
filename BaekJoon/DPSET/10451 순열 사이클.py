import sys
input = sys.stdin.readline
t = int(input())

def dfs(graph, v, visited, end):
	visited[v] = True
	global cnt
	for i in graph[v]:
		if i == end:

			return
		if not visited[i]:
			visited[i] = True

			dfs(graph, i, visited, i)


for _ in range(t):
	cnt = 0
	n = int(input())
	lst = [0] + list(map(int, input().split()))
	visited = [False] * (n+1)
	graph = [[] * (n+1) for _ in range(n+1)]
	for i in range(1, n+1):
		graph[i].append(lst[i])
	for i in range(1, n+1):
		if not visited[i]:
			dfs(graph, i, visited, i)
			cnt += 1
	print(cnt)

