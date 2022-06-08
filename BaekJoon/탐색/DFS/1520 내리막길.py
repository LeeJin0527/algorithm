import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
dp = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, graph):
	if ((x == n-1) and (y == m-1)):
		return 1
	if dp[x][y] != -1:
		return dp[x][y]
	dp[x][y] = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if graph[x][y] > graph[nx][ny]:
			dp[x][y] += dfs(nx, ny, graph)
	return dp[x][y]
cnt = 0
answer = dfs(0, 0, graph)
print(answer)

