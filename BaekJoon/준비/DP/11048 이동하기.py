import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
for i in range(n):
	lst.append([0] + list(map(int, input().split())) +[0])
lst.insert(0, [0] * (m+2))
lst.append([0] * (m+2))

dp = copy.deepcopy(lst)

for i in range(1, n+1):
	for j in range(1, m+1):
		dp[i+1][j] = max(dp[i+1][j], dp[i][j] +lst[i+1][j])
		dp[i][j+1] = max(dp[i][j+1], dp[i][j] + lst[i][j+1])
		dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + lst[i+1][j+1])
print(dp[n][m])