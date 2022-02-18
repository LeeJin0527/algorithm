from collections import deque
m, n, h = map(int, input().split())
graph = [[[]*m for _ in range(n)] for _ in range(h)]


for k in range(h):
	for i in range(n):
		graph[k][i] = list(map(int, input().split()))

q = deque()
for k in range(h):
	for i in range(n):
		for j in range(m):
			if graph[k][i][j] == 1:
				q.append([k, i, j])

dl = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
while q:
	l, x, y = q.popleft()
	for i in range(6):
		nl = l + dl[i]
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m or nl < 0 or nl >= h:
			continue
		if graph[nl][nx][ny] == 0:
			graph[nl][nx][ny] = graph[l][x][y] + 1
			q.append([nl, nx, ny])
answer = 0
for k in range(h):
	for i in range(n):
		for j in range(m):
			if graph[k][i][j] == 0:
				print(-1)
				exit()
			else:
				answer = max(answer, graph[k][i][j])
print(answer-1)


