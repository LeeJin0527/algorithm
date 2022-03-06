import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
dp = [1] * n
for i in range(n):
	for j in range(i):
		if lst[i] >lst[j]:
			dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))