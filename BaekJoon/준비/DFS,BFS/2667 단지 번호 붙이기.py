from collections import deque
import copy
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input())))



visited = [[False]* n for _ in range(n)]

def dfs(x, y):
	global tmp
	if x < 0 or y < 0 or x >= n or y >= n:
		return False
	if graph[x][y] == 1 :
		graph[x][y] = 0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		tmp += 1
		return True
	return False


cnt = 0
result = []
for i in range(n):

	for j in range(n):
		tmp = 0
		if dfs(i, j) == True:
			cnt += 1
			result.append(tmp)
result.sort()
print(cnt)
for i in result:
	print(i)