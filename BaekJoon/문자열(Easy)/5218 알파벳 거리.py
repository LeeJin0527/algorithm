import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	origin, compare = input().split()
	print('Distances:', end = ' ')
	for i in range(len(origin)):
		if ord(origin[i]) <= ord(compare[i]):
			print( ord(compare[i]) - ord(origin[i]) , end = ' ')
		else:
			print( ord(compare[i])+ 26 - ord(origin[i]), end = ' ')
	print()