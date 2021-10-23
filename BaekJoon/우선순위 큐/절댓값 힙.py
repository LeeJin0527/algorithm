import heapq
n = int(input())
graph = []
for i in range(n):
	graph.append(int(input()))
# print(graph)
h = []
for i in graph:
	if i == 0:
		if len(h) == 0:
			print(0)
		else:
			print(heapq.heappop(h)[1])
	else:
		heapq.heappush(h, [abs(i), i])
