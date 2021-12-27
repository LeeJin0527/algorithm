from collections import deque
import sys
n, m, k = map(int, input().split())
INF = int(1e9)
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[INF for _ in range(m)] for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
x1-=1
x2-=1
y1-=1
y2-=1
q = deque()
q.append((x1, y1))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited[x1][y1] = 0
def bfs():
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			nk = 1
			while 0 <= nx < n and 0<= ny< m and nk <= k and graph[nx][ny] == '.' and visited[nx][ny]>visited[x][y]:
				if visited[nx][ny] == INF:
					q.append((nx, ny))
					visited[nx][ny] = visited[x][y] + 1
				nx += dx[i]
				ny += dy[i]
				nk += 1



bfs()
if visited[x2][y2] == INF:
	print(-1)
else:
	print(visited[x2][y2])
