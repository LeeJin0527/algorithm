import sys
origin = list('CAMBRIDGE')

compare = list(sys.stdin.readline().rstrip())

for i in compare:
	if i in origin:
		continue
	else:
		print(i, end = '')