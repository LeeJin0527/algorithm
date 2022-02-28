import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	lst = list(map(int, input().split()))
	dp = [[0] * n for _ in range(n)]
	for x in range(1, n):
		for i in range(n-x):
			j = i + x
			dp[i][j] = 987654321
			tmp = sum(lst[i : j+1])
			for k in range(i, j):
				dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + tmp )
	print(dp[0][n-1])