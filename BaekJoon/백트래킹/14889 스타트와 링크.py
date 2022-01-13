from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
lst = [i for i in range(n)]
result = 987654321
for i in list(combinations(lst, n // 2)):
	start = set(i)
	link = set(lst) - start
	startSum = 0
	linkSum = 0
	for j in list(combinations(start, 2)):
		startSum += graph[j[0]][j[1]]
		startSum += graph[j[1]][j[0]]
	for k in list(combinations(link, 2)):
		linkSum += graph[k[0]][k[1]]
		linkSum += graph[k[1]][k[0]]
	if abs(startSum - linkSum) < result:
		result = abs(startSum - linkSum)
print(result)
