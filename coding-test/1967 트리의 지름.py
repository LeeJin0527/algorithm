import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v-1):
	lst = list(map(int, input().split()))
	graph[lst[0]].append([lst[1], lst[2]])
	graph[lst[1]].append([lst[0], lst[2]])



def dfs(x, y):
	for a, b in graph[x]:
		if visited[a] == -1:
			visited[a] = b + y
			dfs(a, b + y)

visited = [-1] * (v+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
