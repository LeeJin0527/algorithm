import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = []
for i in range(n):
	graph.append(list(input()))
dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]
ans = 0
def dfs(x, y, cnt):
	global ans
	visited[x][y] = cnt
	ans = max(ans, 1)
	for i in range(6):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= n:
			continue
		if graph[nx][ny] == 'X' and visited[nx][ny] == -1:
			dfs(nx, ny, 1-cnt)
			ans = max(ans, 2)
		if visited[nx][ny] == cnt:
			ans = max(ans, 3)


visited = [[-1]* n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if graph[i][j] == 'X' and visited[i][j] == -1:
			dfs(i, j, 0)
print(ans)