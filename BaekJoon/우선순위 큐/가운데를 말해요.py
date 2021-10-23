import heapq
import sys
import time
input = sys.stdin.readline
n = int(input())

left = [] # max heap
right = [] # min heap

for i in range(n):
	tmp = int(input())
	if len(left) == len(right):
		heapq.heappush(left, -tmp)
	else:
		heapq.heappush(right, tmp)
	if right and -left[0] > right[0]:
		lf = -heapq.heappop(left)
		rg = heapq.heappop(right)
		heapq.heappush(left, -rg)
		heapq.heappush(right, lf)
	print(-left[0])
