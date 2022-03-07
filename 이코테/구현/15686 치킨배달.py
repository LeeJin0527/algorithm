from itertools import combinations
import sys
n, m = map(int, input().split())
graph = []
chicken = []
compare = []
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(len(graph[i])):
		if graph[i][j] == 2:
			chicken.append([i, j])
		if graph[i][j] == 1:
			compare.append([i, j])

answer = 0
check = []
for i in list(combinations(chicken, m)):
	check.append(i)
j = 0


result = 987654321

result = 987654321
for j in range(len(check)):
	answer = 0
	for i in compare:

		tmp = 987654321
		for m in check[j]:
			x, y = i
			a, b = m
			tmp = min(tmp, abs(x-a) + abs(y-b))
		answer += tmp

	result = min(result, answer)
print(result)