import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[0] * (m) for _ in range(n)]

q = deque()
q.append([0, 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
	x, y = q.popleft()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if nx >= n or ny >= m or nx < 0 or ny < 0:
			continue
		if visited[nx][ny] == 0 and graph[nx][ny] == 1:
			visited[nx][ny] = visited[x][y] + 1
			q.append([nx, ny])
print(visited[n-1][m-1]+1)