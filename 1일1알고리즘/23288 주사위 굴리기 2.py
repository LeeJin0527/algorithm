import sys
from collections import deque
n, m, k = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
result = 0
x, y = 0, 0
dir = 0
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ball = [2, 4, 1, 3, 5, 6]
def ball_move(x, y, dir):
	nx = x + dx[dir]
	ny = y + dy[dir]
	if check(nx, ny):
		nd = (dir + 2) % 4
		nx = x + dx[nd]
		ny = y + dy[nd]
		return [nx, ny, nd]
	return [nx, ny, dir]

def check(nx, ny):
	if not (0 <= nx < n and 0 <= ny < m):
		return True
	return False

def bfs(r, c):
	count = 1
	q = deque()
	visited = [[False] * m for _ in range(n)]
	q.append([r, c])
	while q:
		x, y = q.popleft()
		visited[x][y] = True
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if check(nx, ny):
				continue
			if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
				visited[nx][ny] = True
				q.append([nx, ny])
				count += 1
	return count


def ball_change(ball, dir):
	# 동
	if dir == 0 :
		ball[1], ball[2], ball[3], ball[5] = ball[5], ball[1], ball[2], ball[3]
	# 남쪽 이동 (전면, 상단, 후면, 바닥)
	elif dir == 1 :
		ball[0], ball[2], ball[4], ball[5] = ball[5], ball[0], ball[2], ball[4]
	# 서쪽 이동 (왼쪽, 상단, 오른쪽, 바닥)
	elif dir == 2 :
		ball[1], ball[2], ball[3], ball[5] = ball[2], ball[3], ball[5], ball[1]
	# 북쪽 이동 (전면, 상단, 후면, 바닥)
	elif dir == 3 :
		ball[0], ball[2], ball[4], ball[5] = ball[2], ball[4], ball[5], ball[0]
	return ball

for _ in range(k):
	# 볼 이동
	x, y, dir = ball_move(x, y, dir)
	ball = ball_change(ball, dir)
	count = bfs(x, y)
	result += count * graph[x][y]
	a, b = ball[5], graph[x][y]
	if a > b :
		dir = (dir + 1) % 4
	elif a < b:
		dir = (dir - 1)
		if dir == -1:
			dir = 3
print(result)