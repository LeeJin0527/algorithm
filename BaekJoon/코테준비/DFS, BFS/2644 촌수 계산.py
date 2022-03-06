import sys
input = sys.stdin.readline
n = int(input())
start, end = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [0] * (n+1)
visited[start] = 1
def dfs(start):
	for i in graph[start]:
		if visited[i] == 0:
			visited[i] = visited[start] + 1
			dfs(i)
	return visited
dfs(start)
if visited[end] == 0:
	print(-1)
else:
	print(visited[end]-1)

