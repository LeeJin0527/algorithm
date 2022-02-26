import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	dp = [0] * (11)

	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	for i in range(4, n+1):
		for j in range(1, 4):
			dp[i] += dp[i-j]

	print(dp[n])
