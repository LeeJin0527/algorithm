import sys
input = sys.stdin.readline
n = int(input())
lst = []
result = 0
for _ in range(n):
	lst.append(list(map(int, input().split())))

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = lst[0][0]
for i in range(1, len(lst)):
	for j in range(len(lst[i])):
		dp[i][j] = max(dp[i-1][j-1]+lst[i][j], dp[i-1][j]+lst[i][j])

result = 0
for i in dp:
	result = max(result, max(i))
print(result)
