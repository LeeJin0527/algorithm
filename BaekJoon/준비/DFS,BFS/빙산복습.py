# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
# 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

check = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
	q = deque()
	q.append([x, y])
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m:
				if graph[nx][ny] == 0:
					count[x][y] += 1
				elif graph[nx][ny] != 0 and not visited[nx][ny]:
					visited[nx][ny] = True
					q.append([nx, ny])
	return 1

year = 0
while True:
	visited = [[False] * m for _ in range(n)]
	count = [[0] * m for _ in range(n)]
	result = []
	for i in range(n):
		for j in range(m):
			if graph[i][j] != 0 and not visited[i][j]:
				visited[i][j] = True
				result.append(bfs(i, j))

	for i in range(n):
		for j in range(m):
			if graph[i][j] != 0 :
				graph[i][j] -= count[i][j]
				if graph[i][j] < 0:
					graph[i][j] = 0

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

