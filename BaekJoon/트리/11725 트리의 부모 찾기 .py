import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
v = int(input())
visited = [False] * (v+1)
parent = [[] for _ in range (v+1)]

for i in range(v-1):
	a, b = map(int, input().split())
	parent[a].append(b)
	parent[b].append(a)

result = [0] * (v+1)

def dfs(parent, i, visited):
	visited[i] = True
	for k in parent[i]:
		if not visited[k]:
			visited[k] = True
			dfs(parent, k, visited)
			result[k] = i


dfs(parent, 1, visited)

for i, v in enumerate(result):
	if i >= 2:
		print(v)
