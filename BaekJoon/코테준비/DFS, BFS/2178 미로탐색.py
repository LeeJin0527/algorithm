import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx =[-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*(m+1) for _ in range(n+1)]
def bfs(a, b):
	q = deque()
	q.append([a, b])
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if visited[nx][ny] == 0 and graph[nx][ny] == 1:
				visited[nx][ny] = visited[x][y]+1
				q.append([nx, ny])
	return visited[n-1][m-1] +1
print(bfs(0, 0))