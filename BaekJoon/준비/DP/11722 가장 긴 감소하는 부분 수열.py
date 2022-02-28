import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * (len(lst))

for i in range(len(lst)):
	for j in range(i+1):
		if lst[j] > lst[i]:
			dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
