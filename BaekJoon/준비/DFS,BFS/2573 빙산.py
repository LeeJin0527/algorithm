import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
year = 0
check = False # 다 녹았는데도 2덩어리 이상이 안나온다.
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
	q.append([x, y])
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m:
				if graph[nx][ny] != 0 and not visited[nx][ny]:
					visited[nx][ny] = True
					q.append([nx, ny])
				elif graph[nx][ny] == 0:
					count[x][y] += 1
	return 1

while True:
	result = []
	visited = [[False] * m for _ in range(n)]
	count = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if graph[i][j] != 0 and not visited[i][j]:
				visited[i][j] = True
				result.append(bfs(i, j))
	for x in range(n):
		for y in range(m):
			graph[x][y] -= count[x][y]
			if graph[x][y] < 0:
				graph[x][y] = 0
	if len(result) == 0:
		break
	if len(result) >= 2:
		check = True
		break
	year += 1

if check:
	print(year)
else:
	print(0)

