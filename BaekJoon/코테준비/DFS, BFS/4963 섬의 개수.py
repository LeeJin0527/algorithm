import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
	if x < 0 or y < 0 or x >= n or y >= m:
		return False
	if graph[x][y] == 1:
		graph[x][y] = 0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		dfs(x-1, y-1)
		dfs(x-1, y+1)
		dfs(x+1, y-1)
		dfs(x+1, y+1)
		return True
	return False


while True:
	m, n = map(int, input().split())
	if n == 0 and m == 0:
		break
	graph = []
	for i in range(n):
		graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
	cnt = 0
	for i in range(n):
		for j in range(m):
			if dfs(i, j) == True:
				cnt += 1
	print(cnt)






