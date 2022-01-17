import sys
import heapq
input = sys.stdin.readline
n = int(input())
'''
1 3
2 4
3 5
'''
lst = []
for i in range(n):
	lst.append(list(map(int, input().split())))
lst.sort(key=lambda x:x[0])

q = []
q.append(lst[0][1])
for i in range(1, n):
	if lst[i][0] < q[0]:
		heapq.heappush(q, lst[i][1])
	else:
		heapq.heappop(q)
		heapq.heappush(q, lst[i][1])
print(len(q))