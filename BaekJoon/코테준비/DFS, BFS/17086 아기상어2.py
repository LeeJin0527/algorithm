import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

v = [[0] * m for _ in range(n)]
q = deque()
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			q.append((i, j))
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
visited = [[False] * m for _ in range(n)]
while q:
	x, y = q.popleft()
	visited[x][y] = True
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if graph[nx][ny] == 0:
			graph[nx][ny] = graph[x][y] + 1
			q.append((nx, ny))
result = -1
for i in graph:
	tmp = max(i)
	if  tmp> result:
		result = tmp
print(result-1)

