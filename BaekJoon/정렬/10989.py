import sys
input = sys.stdin.readline
answer = [0] * 10001
n = int(input())
for i in range(n):
	k = int(input())
	answer[k] += 1
for i, v in enumerate(answer):
	if v != 0:
		for j in range(v):
			print(i)