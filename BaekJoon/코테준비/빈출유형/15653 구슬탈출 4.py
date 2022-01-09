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
	cnt = 0
	while q:
		for _ in range(len(q)):
			rx, ry, bx, by = q.popleft()
			if graph[rx][ry] == 'O':
				return cnt
			for i in range(4):
				rnx = rx
				rny = ry
				bnx = bx
				bny = by
				while True:
					rnx += dx[i]
					rny += dy[i]
					if graph[rnx][rny] == '#':
						rnx -= dx[i]
						rny -= dy[i]
						break
					if graph[rnx][rny] == 'O':
						break
				while True:
					bnx += dx[i]
					bny += dy[i]
					if graph[bnx][bny] == '#':
						bnx -= dx[i]
						bny -= dy[i]
						break
					if graph[bnx][bny] == 'O':
						break
				if graph[bnx][bny] == 'O':
					continue
				if rnx == bnx and rny == bny:
					if abs(rnx-rx) + abs(rny - ry) > abs(bnx-bx) + abs(bny-by):
						rnx -= dx[i]
						rny -= dy[i]
					else:
						bnx -= dx[i]
						bny -= dy[i]
				if not visited[rnx][rny][bnx][bny]:
					visited[rnx][rny][bnx][bny] = True
					q.append((rnx, rny, bnx, bny))
		cnt += 1
	return -1






red = []
blue = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 'R':
			red.append((i, j))
		if graph[i][j] == 'B':
			blue.append((i, j))
visited =[[[[False for _ in range(m)]for _ in range(n)]for _ in range(m)]for _ in range(n)]
q = deque()
q.append((red[0][0], red[0][1], blue[0][0], blue[0][1]))
print(bfs())