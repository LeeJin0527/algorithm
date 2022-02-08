import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
lst = []
for i in range(n):
	lst.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b, visited):
	q = deque()
	q.append((a, b, visited))
	check = [[[0]*2 for _ in range(m)] for _ in range(n)]
	check[a][b][visited] = 1
	while q:
		x, y, v = q.popleft()
		if x == ex-1 and y == ey-1:
			return check[x][y][v]-1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if lst[nx][ny] == 1 and v > 0 and check[nx][ny][v] == 0:
				check[nx][ny][v-1] = check[x][y][v] + 1
				q.append((nx, ny, v-1))
			if lst[nx][ny] == 0 and check[nx][ny][v] == 0:
				check[nx][ny][v] = check[x][y][v] + 1
				q.append((nx, ny, v))
	return -1

print(dfs(hx-1, hy-1, 1))
 
