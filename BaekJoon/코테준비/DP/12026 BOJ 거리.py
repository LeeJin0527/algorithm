import sys
input = sys.stdin.readline
n = int(input())
lst = list(sys.stdin.readline().rstrip())
lst = [0] + lst
INF = int(1e9)
dp = [INF] * (n+1)
dp[1] = 0
# for i, v in enumerate(lst):
for i in range(n+1):
	for j in range(0, i):
		if lst[i] == 'B':
			if lst[j] == 'J':
				if i - j >= 0 :
					dp[i] = min((dp[j] + (i-j) ** 2), dp[i])
				else:
					continue
		elif lst[i] == 'O':
			if lst[j] == 'B':
				if i - j > 0 :
					dp[i] = min((dp[j] + (i-j) ** 2), dp[i])
				else:
					continue
		elif lst[i] == 'J':
			if lst[j] == 'O':
				if i - j > 0 :
					dp[i] = min((dp[j] + (i-j) ** 2), dp[i])
				else:
					continue
if dp[-1] == INF:
	print(-1)
else:
	print(dp[-1])