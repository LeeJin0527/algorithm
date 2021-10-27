from collections import Counter
import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())
prime = [True for _ in range(1000001)]
print(prime[19])
prime[1] = 0
for i in range(2, int(math.sqrt(n))+1):
	if prime[i] == True:
		# print('pp',m)
		x = 2
		while i * x <= n:
			prime[i * x] = False
			x += 1
for i in range(m, n+1):
	if prime[i] == True:
		print(i)