import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
	for j in range(1, m+1):
		if i == 1:
			dp[i][j] = j-1
		elif j == 1:
			dp[i][j] = i-1





for i in range(2, n+1):
	for j in range(2, m+1):
		dp[i][j] = max(dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + 1, dp[i][j])
print(dp[n][m])