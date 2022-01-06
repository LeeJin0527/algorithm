import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
	graph[i+1] = [0] + list(map(int, input().split()))

dp= [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
	for j in range(1, m+1):
		dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i][j-1]+graph[i][j], dp[i-1][j-1] + graph[i][j])
print(dp[n][m])
