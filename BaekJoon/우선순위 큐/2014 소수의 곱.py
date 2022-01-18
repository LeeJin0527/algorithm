import sys
import heapq
input = sys.stdin.readline
# 소수, 번
k, n = map(int, input().split())
lst = list(map(int, input().split()))

q = []
for i in lst:
	heapq.heappush(q, i)

for i in range(n):
	x = heapq.heappop(q)
	for j in lst:
		heapq.heappush(q, x * j)
		if x % j == 0:
			break
print(x)
