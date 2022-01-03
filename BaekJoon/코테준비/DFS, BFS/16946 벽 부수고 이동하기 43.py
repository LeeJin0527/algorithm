import sys
from collections import deque
input  = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
	dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	q = deque()
	q.append([x, y])
	visited[x][y] = 1
	cnt = 1

	while q:
		current_x, current_y = q.pop()
		zeros[current_x][current_y] = group
		for dx, dy in dir:
			next_x, next_y = current_x + dx, current_y + dy
			if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m: continue
			if visited[next_x][next_y]: continue
			if not graph[next_x][next_y]:
				q.append([next_x, next_y])
				visited[next_x][next_y] = 1
				cnt += 1
	return cnt

def countMoves(x, y):
	candidates = set()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
		if not zeros[nx][ny]: continue
		candidates.add(zeros[nx][ny])
	cnt = 1
	for c in candidates:
		cnt += info[c]
		cnt = cnt % 10
	return cnt




info = {}
group = 1
visited = [[0 for _ in range(m)] for _ in range(n)]
zeros = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
	for j in range(m):
		if not graph[i][j] and not visited[i][j]:
			cnt = BFS(i, j)
			info[group] = cnt
			group += 1



answer = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		if graph[i][j]:
			answer[i][j] = countMoves(i, j)
for i in range(n):
	print(''.join(map(str, answer[i])))