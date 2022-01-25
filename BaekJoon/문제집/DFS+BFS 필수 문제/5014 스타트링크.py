import sys
from collections import deque
import sys
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
dx = [u, -d]


q = deque()
q.append(s)
visited = [0] * (1000001)
visit = [False]*(1000001)
def bfs():
	while q:
		x = q.popleft()
		visit[x] = True
		if x == g:
			return visited[x]
		for i in range(2):
			nx = x + dx[i]
			if nx < 1 or nx > f:
				continue
			if visited[nx] == 0 and not visit[nx]:
				visited[nx] = visited[x]+1
				visit[nx] = True
				q.append(nx)
	return 'use the stairs'
print(bfs())
