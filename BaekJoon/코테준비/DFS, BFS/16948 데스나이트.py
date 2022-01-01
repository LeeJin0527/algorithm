import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = [[0] * (n) for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
x, y, a, b = map(int, input().split())

def bfs(a, b, x, y):
	q = deque()
	q.append((a, b))
	while q:
		a, b = q.popleft()
		for i in range(6):
			nx = a + dx[i]
			ny = b + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= n:
				continue
			if lst[nx][ny] == 0:
				q.append((nx, ny))
				lst[nx][ny] += lst[a][b] + 1
	return lst[x][y]
answer = bfs(a, b, x, y)

if answer == 0:
	print(-1)
else:
	print(lst[x][y])
