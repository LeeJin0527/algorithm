import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
	lst = list(map(int, input().split()))
	for j in range(1, len(lst)-2, 2):
		graph[lst[0]].append([lst[j], lst[j+1]])

def dfs(x, y):
	for a, b in graph[x]:
		if visited[a] == -1:
			visited[a] = b + y
			dfs(a, b +y)
visited = [-1] * (v+1)
visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))
visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))
