import sys
while True:
	tmp = sys.stdin.readline().rstrip()
	if tmp == '#':
		break
	else:
		target = tmp[0]
		compare = tmp[1:]
		compare = compare.lower()
		print(target, compare.count(target))


