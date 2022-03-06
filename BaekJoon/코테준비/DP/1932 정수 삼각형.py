import sys
input = sys.stdin.readline
n = int(input())
lst = []
lst.append([0]*(n+1))
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
	lst.append([0] + list(map(int, input().split())) + (n-i-1)*[0])


dp[1][1] = lst[1][1]
for i in range(2, n+1):
	for j in range(1, i+1):

		dp[i][j] = max((lst[i][j] + dp[i-1][j]), (lst[i][j] + dp[i-1][j-1]), dp[i][j])
result = 0
for i in dp:
	result = max(result, max(i))
print(result)