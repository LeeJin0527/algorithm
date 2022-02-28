import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	lst = list(map(int, input().split()))

	q = []
	for i in lst:
		heapq.heappush(q, i)
	if len(q) == 1:
		print(0)
	else:
		answer = 0
		while len(q) > 1:
			tmp1 = heapq.heappop(q)
			tmp2 = heapq.heappop(q)
			answer += tmp1 + tmp2
			heapq.heappush(q, tmp1 + tmp2)
		print(answer)

