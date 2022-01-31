import sys
a = list(input())
b = list(input())
a = [0] + a
b = [0] + b
x = len(a)-1
y = len(b)-1

dp = [[0] * (y+1) for _ in range(x+1)]


for i in range(1, x+1):
	for j in range(1, y+1):
		if a[i] == b[j]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[x][y])

