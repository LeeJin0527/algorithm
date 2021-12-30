n = int(input())
dp = [i for i in range(n+1)]
for i in range(7, n+1):
	for k in range(2, i-2):
		dp[i] = max(dp[i-1]+1, dp[i - (k+1)]* k, dp[i])
print(dp[-1])