import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
info = []
result = []
for i in range(n):
	m, v = map(int, input().split())
	heapq.heappush(info, [m, v])
for i in range(len(info)):
	result.append(heapq.heappop(info))
bag = []
bResult = []
for i in range(k):
	x = int(input())
	heapq.heappush(bag, x)
for i in range(len(bag)):
	bResult.append(heapq.heappop(bag))

i = 0
answer = 0
tmp = []
for j in bResult:
	while i < n and result[i][0] <= j:
		heapq.heappush(tmp, -result[i][1])
		i += 1

	if tmp:
		answer += heapq.heappop(tmp)
print(-answer)




