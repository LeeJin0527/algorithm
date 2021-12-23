from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
indegree = [0] * (n+1)
for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	q = deque()
	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)
	while q:
		now = q.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)
	for i in result:
		print(i, end = ' ')
topology_sort()

 
