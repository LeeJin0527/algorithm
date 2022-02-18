from collections import deque
f, s, g, u, d = map(int, input().split())
q = deque()
q.append([s, 0])
dx = [u, -d]
visited = [False]* 1000001
visited[s] = True
def bfs():
	while q:
		x, cnt = q.popleft()
		if x < 0 or x > 1000001:
			continue
		if x == g:
			return cnt
		for i in range(2):
			nx = x + dx[i]
			if nx < 1 or nx > f:
				continue
			if not visited[nx]:
				visited[nx] = True
				q.append([nx, cnt+1])
	return "use the stairs"
print(bfs())
