import sys
import heapq
input = sys.stdin.readline
n = int(input())
answer = {}
for i in range(n):
	k = int(input())
	if k in answer:
		answer[k] += 1
	else:
		answer[k] = 1

answer = sorted(answer.items(), key= lambda x : (-x[1], x[0]))
print(answer[0][0])
