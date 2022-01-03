import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
lst= []
INF = int(1e9)
for i in range(n):
	lst.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[[0]*(11) for _ in range(1001)] for _ in range(1001)]
visited[0][0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
	ret = INF
	q = deque()
	q.append((0, 0, 0))
	while q:
		x, y, v = q.popleft()
		if x == n-1 and y == m-1:
			ret = min(ret, visited[x][y][v])
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m :continue
			nv = v+1 if lst[nx][ny] == 1 else v
			if nv > k : continue
			if visited[nx][ny][nv] and (visited[nx][ny][nv] <= visited[x][y][v]+1): continue
			# 벽이 있는지
			if lst[nx][ny] == 1:
				if nv > k :continue
				if visited[x][y][v] % 2 == 1:
					visited[nx][ny][nv] = visited[x][y][v]+1
				else:
					visited[nx][ny][nv] = visited[x][y][v]+2
			else:
				visited[nx][ny][nv] = visited[x][y][v]+1
			q.append((nx, ny, nv))
	answer = -1 if ret == INF else ret
	return answer
print(bfs())