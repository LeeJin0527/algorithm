import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
dx = [u, -d]
q = deque()
q.append([s, 0])
visited = [False]*1000001

def bfs():
	while q:
		x, y = q.popleft()
		if x < 1 or x > f:
			continue
		if x == g:
			return y
		for i in range(2):
			nx = x + dx[i]
			if nx < 1 or nx > f:
				continue
			if not visited[nx]:
				visited[nx] = True
				q.append([nx, y+1])
	return "use the stairs"
print(bfs())

