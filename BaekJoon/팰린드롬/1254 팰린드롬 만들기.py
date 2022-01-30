import sys
input = sys.stdin.readline
lst = list(sys.stdin.readline().rstrip())

for i in range(len(lst)):
	compare = reversed(lst[i:])
	if ''.join(list(compare)) == ''.join(lst[i:]):
		print(len(''.join(lst+lst[:i])))
		break
