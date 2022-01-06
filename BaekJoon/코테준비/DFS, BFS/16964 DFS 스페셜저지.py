import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

compare = list(map(int, input().split()))
visited = [False] * ( n+1)
answer = []
def dfs(graph, i, visited):
	visited[i] = True
	answer.append(i)
	for v in graph[i]:
		if not visited[v]:
			dfs(graph, v, visited)
			visited[v] = True
arraySort = [0] * (n+1)
for i in range(len(compare)):
	arraySort[compare[i]] = i
if compare[0] != 1:
	print(0)
	exit()
for i in range(1, len(graph)):
	graph[i].sort(key=lambda x : arraySort[x])
dfs(graph, 1, visited)
if answer == compare:
	print(1)
else:
	print(0)

