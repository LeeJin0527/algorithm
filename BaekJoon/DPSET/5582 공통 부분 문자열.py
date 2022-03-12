import sys

lst = sys.stdin.readline().rstrip()
compare = sys.stdin.readline().rstrip()
dp = [[0] * (len(compare)+1) for _ in range((len(lst)+1))]
answer = 0
for i in range(1, len(lst)+1):
	for j in range(1, len(compare)+1):
		if lst[i-1] == compare[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
			answer = max(answer, dp[i][j])
print(answer)
