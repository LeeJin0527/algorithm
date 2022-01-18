import sys
import heapq
n = int(input())
lst = []
for i in range(n):
	dead, cup = map(int, input().split())
	lst.append([dead, cup])
lst.sort(key=lambda x:(x[0], x[1]))
answer = []
for i, v in enumerate(lst):
	if len(answer) < lst[i][0]:
		heapq.heappush(answer, lst[i][1])
	else:
		if answer[0] < lst[i][1]:
			heapq.heappop(answer)
			heapq.heappush(answer, lst[i][1])
print(sum(answer))