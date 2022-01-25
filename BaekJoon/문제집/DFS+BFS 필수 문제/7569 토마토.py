from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
for i in range(h):
	for j in range(n):
		graph[i].append(list(map(int, input().split())))
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


visited = [[[False]*m for _ in range(n)] for _ in range(h)]
q = deque()

for i in range(h):
	for j in range(n):
		for k in range(m):
			if graph[i][j][k] == 1:
				q.append([i, j, k])

def bfs():
	while q:
		z, x, y = q.popleft()
		for i in range(6):
			nz = z + dz[i]
			nx = x + dx[i]
			ny = y + dy[i]

			if nz < 0 or nz >= h or nx < 0 or ny < 0 or nx >= n or ny >= m  :
				continue

			if graph[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
				visited[nz][nx][ny] = True
				graph[nz][nx][ny] = graph[z][x][y] + 1
				q.append([nz, nx, ny])
bfs()
answer = -1
for i in graph:
	for j in i:
		for k in j:
			if k == 0:
				print(-1)
				exit()
			if k > answer:
				answer = k
print(answer-1)



