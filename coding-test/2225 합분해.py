import sys
input =sys.stdin.readline
n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(n+1):
	dp[i][1] = 1

for i in range(n+1):
	for j in range(2, k+1):
		for h in range(1, j+1):
			dp[i][j] += dp[i-1][h]

print(dp[n][k] % 1000000000)
