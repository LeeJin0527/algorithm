import sys
input =sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (n+1)
if n > k:
	print(0)
	exit()
dp[0] = 1

for j in range(n+1):
	for z in range(j):
		if j + z == k:
			dp[j] += dp[j-z]
print(dp[n])