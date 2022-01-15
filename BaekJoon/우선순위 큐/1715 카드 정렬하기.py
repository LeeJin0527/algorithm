import sys
import heapq
input = sys.stdin.readline
n =  int(input())
lst = []
for i in range(n):
	heapq.heappush(lst, int(input()))
if len(lst) == 1:
	print(0)
else:
	answer = 0
	while len(lst) >1:
		tmp1 = heapq.heappop(lst)
		tmp2 = heapq.heappop(lst)
		answer += tmp1 + tmp2
		heapq.heappush(lst, tmp1 + tmp2)
	print(answer)