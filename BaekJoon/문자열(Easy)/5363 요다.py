import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	lst = list(input().split())
	for i in lst[2:]:
		print(i, end = ' ')
	print(lst[0], lst[1])
