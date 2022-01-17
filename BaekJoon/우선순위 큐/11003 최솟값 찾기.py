import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(m):
	x = heapq.heappop(lst)
	y = heapq.heappop(lst)
	mid = x+ y
	heapq.heappush(lst, mid)
	heapq.heappush(lst, mid)
print(sum(lst))