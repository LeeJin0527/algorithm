import sys
from collections import deque
n = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(n-1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

compare = list(map(int, input().split()))
visited = [False] * (n+1)
answer = []
def bfs(start, graph, visited):
	q = deque()
	q.append(start)
	visited[start] = True
	while q:
		x = q.popleft()
		answer.append(x)
		for i in graph[x]:
			if not visited[i]:

				q.append(i)
				visited[i] = True


if compare[0] != 1:
	print(0)
	exit()


q = deque()
q.append(1)
arraySort = [0]*(n+1)
for i in range(len(compare)):
	arraySort[compare[i]] = i

for i in range(1, len(graph)):
	graph[i].sort(key=lambda x:arraySort[x])
bfs(1, graph, visited)
if answer == compare:
	print(1)
else:
	print(0)
