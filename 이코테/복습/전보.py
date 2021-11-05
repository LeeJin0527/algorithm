import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
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
count = 0
max_distance = 0
for i in range(1, n+1):
	if distance[i] != INF:
		count += 1
		max_distance = max(max_distance, distance[i])
print(count-1, max_distance)


