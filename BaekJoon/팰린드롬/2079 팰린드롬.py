lst = list(input())
n = len(lst)
lst = [0] + lst
palin = [[False]* (n+1) for _ in range(n+1)]
dp = [0] * (n+1)
for i in range(1, n+1):
	palin[i][i] = True
for i in range(1, n):
	if lst[i] == lst[i+1]:
		palin[i][i+1] = True
for j in range(2, n):
	i = 1
	while True:
		if i+j > n:
			break
		if lst[i] == lst[i+j] and palin[i+1][i+j-1]:
			palin[i][i+j] = True
		i += 1
dp[0] = 0
for i in range(1, n+1):
	dp[i] = int(1e9)
	for j in range(1, i+1):
		if palin[j][i]:
			dp[i] = min(dp[i], dp[j-1]+1)
print(dp[n])