import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
graph= []
for i in range(n):
	graph.append(list(map(int,sys.stdin.readline().rstrip())))
INF = int(1e9)
visited = [[INF]* m for _ in range(n)]
visited[0][0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
	q = deque()
	q.append((0, 0))
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if visited[nx][ny] != INF and visited[nx][ny] <= visited[x][y]+1:
				continue
			if graph[nx][ny] == 1 and visited[nx][ny] == INF:
				visited[nx][ny] = visited[x][y]+1
				q.append((nx, ny))
			elif graph[nx][ny] == 0 and visited[nx][ny] == INF:
				visited[nx][ny] = visited[x][y]
				q.appendleft((nx, ny))
	return visited[n-1][m-1]

print(bfs())