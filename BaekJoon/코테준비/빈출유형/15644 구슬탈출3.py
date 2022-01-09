import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
moveTypes = ['U','D','L','R']
def bfs():
	cnt = 1
	while q:
		for _ in range(len(q)):
			rx, ry, bx, by, d = q.popleft()
			visited[rx][ry][bx][by] = True
			for i in range(4):
				rnx = rx
				rny = ry
				while True:
					rnx += dx[i]
					rny += dy[i]
					if graph[rnx][rny] == "#":
						rnx -= dx[i]
						rny -= dy[i]
						break
					if graph[rnx][rny] == "O":
						break

				bnx = bx
				bny = by
				while True:
					bnx += dx[i]
					bny += dy[i]
					if graph[bnx][bny] == "#":
						bnx -= dx[i]
						bny -= dy[i]
						break
					if graph[bnx][bny] == "O":
						break
				if graph[bnx][bny] == "O":
					continue
				if graph[rnx][rny] == "O":
					print(cnt)
					print(d + moveTypes[i])
					return

				if rnx == bnx and rny == bny:
					if abs(rnx-rx) + abs(rny-ry) > abs(bnx-bx) + abs(bny-by):
						rnx -= dx[i]
						rny -= dy[i]
					else:
						bnx -= dx[i]
						bny -= dy[i]
				if not visited[rnx][rny][bnx][bny]:
					visited[rnx][rny][bnx][bny] = True
					q.append((rnx, rny, bnx, bny, d + moveTypes[i]))
		cnt += 1
		if cnt > 10:
			print(-1)
			return
	print(-1)
	return


red = []
blue = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 'R':
			red.append((i, j))
		if graph[i][j] == 'B':
			blue.append((i, j))
q = deque()
q.append((red[0][0], red[0][1], blue[0][0], blue[0][1], ''))
visited = [[[[False for _ in range(m)]for _ in range(n)]for _ in range(m)]for _ in range(n)]

bfs()