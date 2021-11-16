import math
n = int(input())
lst = list(map(int, input().split()))
lst.sort()

prime = [False] * 1001
prime[1] = True
for i in range(2, int(math.sqrt(lst[-1]))+1):
	j = 2
	while i * j <= max(lst) and prime[i] == False:
		prime[i*j] = True
		j += 1
cnt = 0
for i in lst:
	if prime[i] == False:
		cnt += 1
print(cnt)
