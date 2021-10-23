import heapq
n = int(input())
h = []
graph = []
for i in range(n):
	graph.append(int(input()))

last = []
for i in graph:
	if i == 0:
		if len(h) == 0:
			print(0)
		else:
			print(heapq.heappop(h))
	else:
		heapq.heappush(h, i)






