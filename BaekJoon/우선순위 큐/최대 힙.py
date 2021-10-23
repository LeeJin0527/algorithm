import heapq
n = int(input())
graph = []
for i in range(n):
	graph.append(int(input()))
h = []
for i in graph:
	if i == 0:
		if len(h) == 0:
			print(0)
		else:
			answer = heapq.heappop(h)
			print(-answer)
	else:
		heapq.heappush(h, -i)