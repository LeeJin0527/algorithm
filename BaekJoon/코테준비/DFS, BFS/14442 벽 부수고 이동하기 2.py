import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
lst = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b, visit):
	q = deque()
	q.append((a, b, visit))
	visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
	visited[0][0][k] = 1
	while q:
		x, y, v = q.popleft()
		if x == n-1 and y == m-1:
			return visited[x][y][v]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if lst[nx][ny] == 1 and v > 0 and visited[nx][ny][v-1] == 0:
				visited[nx][ny][v-1] = visited[x][y][v] + 1
				q.append((nx, ny, v-1))

			if lst[nx][ny] == 0 and visited[nx][ny][v] == 0:
				visited[nx][ny][v] = visited[x][y][v] + 1
				q.append((nx, ny, v))
	return -1
print(bfs(0, 0, k))