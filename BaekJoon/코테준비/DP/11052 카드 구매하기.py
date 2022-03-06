import sys
input = sys.stdin.readline
n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = lst[1]
for i in range(2, n+1):
	for j in range(1, i+1):
		dp[i] = max(lst[i], (dp[i-j] + dp[j]), dp[i])
print(dp[n])