import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
	lst = list(map(int, input().split()))
	for j in lst:
		heapq.heappush(q, j)
		if len(q) > n:
			heapq.heappop(q)
print(q[0])