import sys
import copy
from collections import deque
input= sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

while True:
	cnt += 1
	removeCnt = [[0]*m for _ in range(n)]
	for x in range(n):
		for y in range(m):
			if graph[x][y] > 0:
				for i in range(4):
					nx = x + dx[i]
					ny = y + dy[i]
					if nx < 0 or ny < 0 or nx >= n or ny >= m:
						continue
					if graph[nx][ny] == 0:
						removeCnt[x][y] += 1
	for i in range(n):
		for j in range(m):
			if graph[i][j] > 0 :
				graph[i][j] -= removeCnt[i][j]
				if graph[i][j] < 0 :
					graph[i][j] = 0
	cntIsland = 0
	visited = [[False]*m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if graph[i][j] > 0 and not visited[i][j]:
				cntIsland += 1
				visited[i][j] = True
				q = [[i, j]]
				while q:
					x, y = q.pop()
					for k in range(4):
						nx = x + dx[k]
						ny = y + dy[k]
						if nx < 0 or ny < 0 or nx >= n or ny >= m:
							continue
						if graph[nx][ny] > 0 and not visited[nx][ny]:
							visited[nx][ny] = True
							q.append([nx, ny])
	if cntIsland >= 2:
		break
	total = 0
	for i in graph:
		total += sum(i)

	if total == 0:
		print(0)
		exit()
print(cnt)

