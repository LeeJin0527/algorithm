import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
rev_lst = lst[::-1]
lst = [0] + lst
rev_lst = [0] + rev_lst
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		if lst[i] == rev_lst[j]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(n - dp[n][n])
