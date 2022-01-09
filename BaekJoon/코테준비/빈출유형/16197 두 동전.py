import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
	while q:
		x1, y1, x2, y2, cnt = q.popleft()
		if cnt >= 10:
			return -1
		for i in range(4):
			nx1 = x1 + dx[i]
			ny1 = y1 + dy[i]
			nx2 = x2 + dx[i]
			ny2 = y2 + dy[i]
			if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
				if graph[nx1][ny1] == "#":
					nx1, ny1 = x1, y1
				if graph[nx2][ny2] == "#":
					nx2, ny2 = x2, y2
				if not visited[nx1][ny1][nx2][ny2]:
					visited[nx1][ny1][nx2][ny2] = True
					q.append((nx1, ny1, nx2, ny2, cnt+1))
			elif 0 <= nx1 < n and 0 <= ny1 < m:
				return cnt+1
			elif 0 <= nx2 < n and 0 <= ny2 < m:
				return cnt
			else:
				continue
	return -1
start = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == "o":
			start.append([i, j])
q = deque()
q.append((start[0][0], start[0][1], start[1][0], start[1][1], 0))
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
print(bfs())
