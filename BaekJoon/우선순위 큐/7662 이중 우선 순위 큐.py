import sys
import heapq
input = sys.stdin.readline
t = int(input())
for i in range(t):
	n = int(input())
	min_heap = []
	max_heap = []
	visited = [False] * n
	for j in range(n):
		x, y = input().split()
		if x == 'I':
			heapq.heappush(min_heap, (int(y), j))
			heapq.heappush(max_heap, (-int(y), j))
			visited[j] =True
		else:
			if int(y) == 1:
				while max_heap and visited[max_heap[0][1]] == False:
					heapq.heappop(max_heap)
				if max_heap:
					visited[max_heap[0][1]] = False
					heapq.heappop(max_heap)
			elif int(y) == -1:
				while min_heap and visited[min_heap[0][1]] == False:
					heapq.heappop(min_heap)
				if min_heap:
					visited[min_heap[0][1]] = False
					heapq.heappop(min_heap)
	if True not in visited:
		print('EMPTY')
	else:
		while max_heap and visited[max_heap[0][1]] == False:
			heapq.heappop(max_heap)
		while min_heap and visited[min_heap[0][1]] == False:
			heapq.heappop(min_heap)
		print(-max_heap[0][0], min_heap[0][0])
