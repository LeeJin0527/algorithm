import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
dx = [-1, 1, 2]
visited = []
def bfs(x, time):
	q = deque()
	q.append([x, time])
	visited.append(x)
	while q:
		x, y = q.popleft()

		if x > 100000 or x < 0:
			continue
		if x == k:
			return y
		for i in range(3):
			if i == 2:
				nx = x * dx[i]
			else:
				nx = x + dx[i]
			if nx < 0 or nx > 100000:
				continue
			if nx not in visited:
				visited.append(nx)
				q.append([nx, y+1])

print(bfs(n, 0))