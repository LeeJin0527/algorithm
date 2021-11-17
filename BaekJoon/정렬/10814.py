import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
	x, y = input().split()
	answer.append((int(x), y))
answer = sorted(answer, key = lambda x : x[0])

for i in answer:
	for j in i:
		print(j, end = ' ')
	print()