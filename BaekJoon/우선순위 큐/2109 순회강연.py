import sys
import heapq
input= sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
	p, d = map(int, input().split())
	lst.append([d, p])
lst.sort(key=lambda x:(x[0], x[1]))
answer = []
for i in range(len(lst)):
	if len(answer) < lst[i][0]:
		heapq.heappush(answer, lst[i][1])
	else:
		if lst[i][1] > answer[0]:
			heapq.heappop(answer)
			heapq.heappush(answer, lst[i][1])
print(sum(answer))