import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] *( v+1)
for i in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
def dijkstra(start):
	q = []
	distance[start] = 0
	heapq.heappush(q, (0, start))
	while q:
		dist, now = heapq.heappop(q)
		if dist < distance[now]:
			continue
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))
dijkstra(start)
for i in range(1, v+1):
	if distance[i] == INF:
		print('INF')
	else:
		print(distance[i])