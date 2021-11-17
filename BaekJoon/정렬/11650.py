import sys
input = sys.stdin.readline
n = int(input())
answer = [[] for _ in range(-100001, 100001)]

for i in range(n):
	x, y = map(int, input().split())
	answer[x].append(y)


for i in range(-100000, 100001):
	if len(answer[i]) != 0:
		answer[i].sort()
		for j in answer[i]:
			print(i, j)