from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 2]
q = deque()
q.append([n, 0])

visited = [False] * 300001
visited[n] = True
while q:
	x, time = q.popleft()
	if x == m:
		print(time)
		break
	if x > 100001:
		continue
	for i in range(3):
		if i == 2:
			nx = x * dx[i]
		else:
			nx = x + dx[i]

		if nx < 0 or nx > 300001:
			continue
		if not visited[nx]:
			visited[nx] =True
			q.append([nx, time+1])
