import math
m = int(input())
n = int(input())
prime = [False] * 10001
prime[0] = True
prime[1] = True

for i in range(2, int(math.sqrt(n)) + 1):
	j = 2
	if prime[i] == False:
		while i * j <= n:
			prime[i * j] = True
			j += 1
result = 0
answer = 10001
for i in range(m, n+1):
	if prime[i] == False:
		answer = min(i, answer)
		result += i

if answer == 10001:
	print(-1)
	exit()
print(result)
print(answer)

