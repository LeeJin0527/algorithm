import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[]* (n+1) for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

q = deque([1])
visited = [False] * (n+1)
answer = []
while q:
	x = q.popleft()
	answer.append(x)
	visited[x] = True
	for i in graph[x]:
		if not visited[i]:
			visited[i] = True
			q.append(i)
print(len(answer) -1)