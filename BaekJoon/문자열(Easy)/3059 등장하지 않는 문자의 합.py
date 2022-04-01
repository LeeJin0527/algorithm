import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	lst = list(sys.stdin.readline().rstrip())
	answer = 0
	for i in range(65, 91):
		if chr(i) not in lst:
			answer += i
	print(answer)