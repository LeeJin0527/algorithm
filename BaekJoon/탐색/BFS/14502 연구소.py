from itertools import combinations
from collections import deque
import copy
import time
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
virusList =[]
mediList = []



for i in range(n):
	graph.append(list(map(int, input().split())))
for i in range(n):
	for j in range(m):
		if graph[i][j] == 2:
			virusList.append((i, j))
		elif graph[i][j] == 0:
			mediList.append((i, j))

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if tmp[nx][ny] == 1 or tmp[nx][ny] == 2:
				continue
			if tmp[nx][ny] == 0:
				tmp[nx][ny] = 2
				queue.append((nx, ny))
	return tmp
# start = time.time()
answer = 0
for i in combinations(mediList, 3):
	tmp = copy.deepcopy(graph)
	for x, y in i:
		tmp[x][y] = 1

	for x, y in virusList:
		tmp = bfs(x, y)

	cnt = 0
	for i in tmp:
		cnt += i.count(0)
	if cnt > answer:
		answer = cnt
	# print(cnt)
print(answer)
