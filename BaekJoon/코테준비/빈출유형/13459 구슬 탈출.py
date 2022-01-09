import sys
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
RED = []
BLUE = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(rx, ry, bx, by):
	visited[rx][ry][bx][by] = True
	cnt = 0
	while q:
		for _ in range(len(q)):
			redX, redY, blueX, blueY = q.popleft()
			if cnt > 10:
				return 0
			if graph[redX][redY] == "O":
				return 1
			for i in range(4):
				redNX = redX
				redNY = redY
				# 빨간색 구슬
				while True:
					redNX += dx[i]
					redNY += dy[i]
					if graph[redNX][redNY] == "#":
						redNX -= dx[i]
						redNY -= dy[i]
						break
					if graph[redNX][redNY] == "O":
						break
				# 파란색 구슬
				blueNX = blueX
				blueNY = blueY
				while True:
					blueNX += dx[i]
					blueNY += dy[i]
					if graph[blueNX][blueNY] == "#":
						blueNX -= dx[i]
						blueNY -= dy[i]
						break
					if graph[blueNX][blueNY] == "O":
						break
				if graph[blueNX][blueNY] == "O":
					continue
				if redNX == blueNX and redNY == blueNY:
					if abs(redNX - redX) + abs(redNY - redY) > abs(blueNX - blueX) + abs(blueNY - blueY):
						redNX -= dx[i]
						redNY -= dy[i]
					else:
						blueNX -= dx[i]
						blueNY -= dy[i]
				if not visited[redNX][redNY][blueNX][blueNY]:
					visited[redNX][redNY][blueNX][blueNY] = True
					q.append((redNX, redNY, blueNX, blueNY))
		cnt += 1
	return 0

for i in range(n):
	for j in range(m):
		if graph[i][j] == 'R':
			RED.append((i, j))
		if graph[i][j] == 'B':
			BLUE.append((i, j))
q = deque()
q.append((RED[0][0], RED[0][1], BLUE[0][0], BLUE[0][1]))
visited = [[[[False for _ in range(m)] for _ in range(n)]for _ in range(m)]for _ in range(n)]
print(bfs(RED[0][0], RED[0][1], BLUE[0][0], BLUE[0][1]))