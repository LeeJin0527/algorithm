import math
n = int(input())
prime = [True for _ in range(1001)]
lst = list(map(int, input().split()))
prime[0] = False
prime[1] = False
m = max(lst)
for i in range(2, int(math.sqrt(m)) + 1):
	j = 2
	if prime[i] == True:
		while i * j <= m:
			prime[i * j] = False
			j += 1
# print(prime)
cnt = 0
for i in lst:
	if prime[i] == True:
		cnt += 1
print(cnt)

