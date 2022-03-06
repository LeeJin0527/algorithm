import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
	global cnt
	if x < 0 or y < 0 or x >= n or y >= n:
		return False
	if graph[x][y] == 1 and not visited[x][y]:
		visited[x][y] = True
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		cnt += 1
		return True
	return False

result = []
for i in range(n):
	for j in range(n):
		cnt = 0
		if dfs(i, j) == True:
			cnt += 1
			result.append(cnt-1)

result.sort()
print(len(result))
for i in result:
	print(i)

