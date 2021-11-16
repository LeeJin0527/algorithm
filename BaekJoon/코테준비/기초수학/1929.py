import math
prime = [False] * 1000001
prime[1] = True
n, m = map(int, input().split())
for i in range(2, int(math.sqrt(m))+1):
	j = 2
	while i*j <= m and prime[i] == False:
		prime[i*j] = True
		j += 1
for i in range(n, m+1):
	if prime[i] == False:
		print(i)