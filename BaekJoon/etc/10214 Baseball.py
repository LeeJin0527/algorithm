import sys
input = sys.stdin.readline
t = int(input())
korea = 0
yonsei = 0
for i in range(t):
	for j in range(9):
		x, y = map(int, input().split())
		yonsei += x
		korea += y
	if korea > yonsei:
		print('Korea')
	elif korea < yonsei:
		print('Yonsei')
	else:
		print('Draw')