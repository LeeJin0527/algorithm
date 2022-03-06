from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
visited = [[[0]*m for _ in range(n)] for _ in range(h)]

graph = [[[]*m for _ in range(n)]for _ in range(h)]
for x in range(h):
	for i in range(n):
		graph[x][i] = (list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()
for x in range(h):
	for i in range(n):
		for j in range(m):
			if graph[x][i][j] == 1:
				q.append([x, i, j])

while q:
	z, x, y = q.popleft()
	for i in range(6):
		nz = z + dz[i]
		nx = x + dx[i]
		ny = y + dy[i]

		if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
			continue
		if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:

			visited[nz][nx][ny] = visited[z][x][y] + 1

			q.append([nz, nx, ny])
for x in range(h):
	for i in range(n):
		for j in range(m):
			if graph[x][i][j] == 1 or graph[x][i][j] == -1:
				continue
			else:
				if visited[x][i][j] == 0:
					print(-1)
					exit()
answer = 0

for x in range(h):
	for i in range(n):
		answer = max(answer, max(visited[x][i]))
print(answer)


