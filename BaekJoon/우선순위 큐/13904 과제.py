import sys
import heapq
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
	left, cost = map(int, input().split())
	lst.append((left, cost))
lst.sort(key=lambda x:x[0])
answer = []
for i in range(len(lst)):
	if len(answer) <= lst[i][0]-1:

		heapq.heappush(answer, lst[i][1])
	else:
		if answer[0] < lst[i][1]:
			heapq.heappop(answer)
			heapq.heappush(answer, lst[i][1])
print(sum(answer))
