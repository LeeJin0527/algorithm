import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	for start in range(n-i):
		end = start+i
		if start == end:
			dp[start][end] =1
		else:
			if start +1 == end and lst[start] == lst[end]:
				dp[start][end] = 1
			elif dp[start+1][end-1] == 1 and lst[start] == lst[end]:
				dp[start][end] = 1
for i in range(m):
	a, b = map(int, input().split())
	print(dp[a-1][b-1])