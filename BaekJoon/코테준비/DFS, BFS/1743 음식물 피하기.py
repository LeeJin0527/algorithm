import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)]for _ in range(n)]

for i in range(k):
	x, y = map(int, input().split())
	graph[x-1][y-1] = 1


def dfs(x, y):
	global each
	if x < 0 or y < 0 or x >= n or y >= m:
		return False
	if graph[x][y] == 0:
		return False
	if graph[x][y] == 1:
		graph[x][y] = 0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		each += 1
		return True
	return False

answer = []
for i in range(n):
	for j in range(m):
		each = 0
		if dfs(i, j) == True:
			answer.append(each)

print(max(answer))
