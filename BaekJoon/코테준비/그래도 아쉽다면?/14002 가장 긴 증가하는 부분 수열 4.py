import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
d = [0] * n
for i in range(n):
	for j in range(i):
		if lst[i] > lst[j]:
			dp[i] = max(dp[i], dp[j]+1)
maxVal = max(dp)
res = []
for i in range(len(dp)-1, -1, -1):
	if dp[i] == maxVal:
		res.append(lst[i])
		maxVal -= 1
res.reverse()
print(max(dp))
print(*res)
