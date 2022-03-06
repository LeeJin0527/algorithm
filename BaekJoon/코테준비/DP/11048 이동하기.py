import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
lst.append([0] * (m+1))
for i in range(n):
	lst.append([0] +list(map(int, input().split())))
lst.append([0]*(m+1))

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
	for j in range(1, m+1):
		dp[i][j] = max(dp[i-1][j]+ lst[i][j], dp[i][j-1] + lst[i][j], dp[i-1][j-1] + lst[i][j])
print(dp[n][m])