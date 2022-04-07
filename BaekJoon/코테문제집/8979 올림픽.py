import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))


answer = sorted(lst, key=lambda x: (-x[1], -x[2], -x[3]))


for i in range(n):
	if answer[i][0] == k:
		index = i
for i in range(n):
	if answer[index][1:] == answer[i][1:]:
		print(i+1)
		break