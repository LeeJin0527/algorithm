import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	dp = [0] * (n+1)
	for i in range(2, n+1):
		k = i
		while k < n+1:
			if dp[k] == 0:
				dp[k] = 1
			else:
				dp[k] = 0
			k += i
	cnt = 0
	for i in range(1, len(dp)):
		if dp[i] == 0:
			cnt +=1
	print(cnt)
