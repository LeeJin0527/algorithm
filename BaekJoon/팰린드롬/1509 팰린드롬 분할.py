lst = list(input())
n = len(lst)
lst = [0] + lst

# 맨 앞자리와 맨 뒷자리가 같고, 그 사이 값이 팰린드롬 이면 팰린드롬임
# DP를 한번 더 돌려서 팰린드롬 분할 -> 갯수가 최소 , 팰린드롬 길이 최대
dp = [0] * (n+1)

palin = [[False] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
	if lst[i] == lst[i]:
		palin[i][i] = True

for i in range(1, n):
	if lst[i] == lst[i+1]:
		palin[i][i+1] = True
	else:
		palin[i][i+1] = False

for j in range(2, n):
	i = 1
	while True:
		if i+j > n:
			break
	# for i in range(1, i+j <= n):
		if lst[i] == lst[i+j] and palin[i+1][i+j-1]:
			palin[i][i+j] = True
		i += 1

dp[0] = 0
for i in range(1, n+1):
	dp[i] = int(1e9)
	for j in range(1, i+1):
		if palin[j][i] :
			dp[i] = min(dp[i], dp[j-1]+1)
print(dp[n])





