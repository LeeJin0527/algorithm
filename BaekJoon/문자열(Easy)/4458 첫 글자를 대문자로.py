import sys
t = int(input())
for _ in range(t):
	lst = list(sys.stdin.readline().rstrip())
	lst[0] = lst[0].upper()
	print(''.join(lst))