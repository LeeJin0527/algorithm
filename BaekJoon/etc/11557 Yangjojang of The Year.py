import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
	n = int(input())
	lst = []
	for i in range(n):
		lst.append(list(input().split()))
	lst.sort(key=lambda x:-int(x[1]))
	print(lst[0][0])