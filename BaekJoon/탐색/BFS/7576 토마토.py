from collections import deque
m, n = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			q.append((i, j))

def bfs():
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if graph[nx][ny] == -1:
				continue
			if graph[nx][ny] == 0:
				q.append((nx, ny))
				graph[nx][ny] = graph[x][y] + 1
	return graph


bfs()
answer = 0
for i in graph:
	for j in i:
		if j == 0:
			print(-1)
			exit()
		else:
			answer = max(answer, j)
print(answer-1)