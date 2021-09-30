from collections import deque
n, k = map(int, input().split())
dx = [2, 1, -1]
come = [0 for _ in range(200001)]
visited = [False] * 200001
def bfs(x):
	queue = deque([x])
	visited[x] = True
	while queue:
		v = queue.popleft()
		if v == k:
			break
		if v > 100001:
			continue
		for i, h in enumerate(dx):
			if i == 0:
				nx = v * h
			else:
				nx = v + h
			if nx < 0 or nx > 200001:
				continue
			if visited[nx] == True:
				continue
			else:
				visited[nx] = True
				queue.append(nx)
				come[nx] = come[v] + 1
	return come[v]
print(bfs(n))