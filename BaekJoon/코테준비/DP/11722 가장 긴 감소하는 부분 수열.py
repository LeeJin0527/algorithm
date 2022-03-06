import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * 1001
for i in range(n):
	for j in range(i+1):
		if lst[i] < lst[j]:
			dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))