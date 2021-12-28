import sys
input = sys.stdin.readline
n = int(input())
t = []
p = []
for i in range(n):
	x, y = map(int, input().split())
	t.append(x)
	p.append(y)
t = [0] + t
p = [0] + p
dp = [0] * 1500003
for i in range(n, 0, -1):
	if i + t[i] > n+1:
		dp[i] = dp[i+1]
	else:
		dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])
print(dp[1])