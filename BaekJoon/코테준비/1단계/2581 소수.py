import sys
import math
input = sys.stdin.readline
m = int(input())
n = int(input())
prime = [True for _ in range(10001)]
prime[1] = False


for i in range(2,int(math.sqrt(n))+1 ):
	j = 2
	if prime[i] == True:
		while i* j <= n:
			prime[i*j] = False
			j += 1
tmp = 0
answer = []
for i in range(m, n+1):
	if prime[i] == True:
		answer.append(i)
		tmp += i
if len(answer) == 0:
	print('-1')
else:
	print(tmp)
	print(min(answer))


