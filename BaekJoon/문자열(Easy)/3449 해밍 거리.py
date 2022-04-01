import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	origin = list(input().rstrip())
	compare = list(input().rstrip())

	answer = 0
	for i in range(len(origin)):
		if origin[i] != compare[i]:
			answer += 1
	print('Hamming distance is',str(answer)+'.')