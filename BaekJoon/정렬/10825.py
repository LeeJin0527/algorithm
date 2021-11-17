import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
	name, korean, english, math = input().split()
	answer.append((name, int(korean), int(english), int(math)))
answer = sorted(answer, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in answer:
	print(i[0])