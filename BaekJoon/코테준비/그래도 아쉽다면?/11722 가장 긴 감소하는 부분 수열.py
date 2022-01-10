import sys
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * (n)
for i in range(n):
	for j in range(i):
		if lst[i] < lst[j]:
			dp[i] = max(dp[i], dp[j]+1)
print(max(dp))