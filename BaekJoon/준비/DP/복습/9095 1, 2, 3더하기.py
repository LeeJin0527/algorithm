import sys
n = int(input())
test = []
for i in range(n):
	test.append(int(input()))
# dp 리스트 만들어 줄 것
dp = [0] * (max(test) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in test:
	print(dp[i])
