import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
k = max(lst)

dp = [True] * (k+1)
dp[0] = False
for i in range(2, k+1):
	j = 1
	while i*j <= k:

		if dp[i*j] == True:
			dp[i*j] = False
		else:
			dp[i*j] = True
		j += 1
for i in lst:
	tmp = dp[:i+1]
	print(tmp.count(1))
