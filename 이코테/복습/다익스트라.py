n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
visited = [False] * (n+1)
distance = [INF] * (n+1)
graph = [[ ] for _ in range(n+1)]
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
def get_smallest_node():
	index = 0
	min_value = INF
	for i in range(1, n+1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index
def dijkstra(start):
	visited[start] = True
	distance[start] = 0
	for i in graph[start]:
		distance[i[0]] = i[1]
	for j in range(n-1):
		now = get_smallest_node()
		visited[now] = True
		for i in graph[now]:
			cost = distance[now] + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost

dijkstra(start)
for i in range(1, n+1):
	if distance[i] == INF:
		print('INF')
	else:
		print(distance[i])