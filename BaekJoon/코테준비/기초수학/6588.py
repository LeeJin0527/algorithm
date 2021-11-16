import math
import sys
sys = sys.stdin.readline

prime = [False] * 1000001
prime[1] = True
answer = []
while True:
	x = int(input())
	if x == 0:
		break
	answer.append(x)
tmp = max(answer)

for i in range(2, int(math.sqrt(tmp))+1):
	j = 2
	if prime[i] == False :
		while i * j <= tmp:
			prime[i*j] = True
			j += 1
for i in answer:
	for j in range(3, i):
		if prime[j] == False and prime[i-j] == False:
			print(str(i), '=', str(j),'+',str(i-j))
			break
