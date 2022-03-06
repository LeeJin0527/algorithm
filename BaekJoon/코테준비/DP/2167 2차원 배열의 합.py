import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
lst.append([0]*(m+1))

for i in range(n):
	lst.append([0] + list(map(int, input().split())))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = lst[1][1]
for i in range(1, n+1):
	for j in range(1, m+1):
		if i == 1:
			dp[i][j] = dp[i][j-1] + lst[i][j]
		if j == 1:
			dp[i][j] = dp[i-1][j] + lst[i][j]
		else:
			dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + lst[i][j]

k = int(input())
for _ in range(k):
	i, j, x, y = map(int, input().split())
	print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])