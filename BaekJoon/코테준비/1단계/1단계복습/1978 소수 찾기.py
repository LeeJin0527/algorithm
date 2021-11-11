import math
n = int(input())
lst = list(map(int, input().split()))
prime = [False] * 1001
prime[0] = True
prime[1] = True
m = max(lst)
for i in range(2, int(math.sqrt(m)) +1):
	j = 2
	if prime[i] == False:
		while i * j <= m:
			prime[i * j] = True
			j += 1
cnt = 0
for i in lst:
	if prime[i] == False:
		cnt += 1
print(cnt)