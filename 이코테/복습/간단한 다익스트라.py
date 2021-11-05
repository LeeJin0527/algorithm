v, e = map(int, input().split())
start = int(input())
graph = [[]  for _ in range(v+1)]
INF = int(1e9)
visited = [False] * (v+1)
distance = [INF] * (v+1)

for i in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
def get_smallest_node():
	index = 0
	min_value = INF
	for i in range(1, v+1):
		if not visited[i] and min_value > distance[i]:
			min_value = distance[i]
			index = i
	return index

def dijkstra(start):
	visited[start] = True
	distance[start] = 0
	for i in graph[start]:
		distance[i[0]] = i[1]

	for i in range(v-1):
		now = get_smallest_node()
		visited[now] = True
		for j in graph[now]:
			cost = distance[now] + j[1]
			if cost < distance[j[0]]:
				distance[j[0]] = cost

dijkstra(start)
for i in range(1, v+1):
	if distance[i] == INF:
		print('INF')
	else:
		print(distance[i])