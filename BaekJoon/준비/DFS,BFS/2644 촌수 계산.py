import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
i, j = map(int, input().split())

graph = [[]* (n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)


visited = [False] * (n+1)
q = deque([i])
result = [0] *(n+1)
while q:
	x = q.popleft()
	visited[x] = True
	for i in graph[x]:
		if visited[i] == False:
			visited[i] = True
			result[i] = result[x] + 1
			q.append(i)
if result[j] == 0:
	print(-1)
else:
	print(result[j])


