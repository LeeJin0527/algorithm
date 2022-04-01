import sys
lst = list(sys.stdin.readline().rstrip())
for i, v in enumerate(lst):
	if 65 <= ord(v) < 92:
		lst[i] = v.lower()
	else:
		lst[i] = v.upper()
print(''.join(lst))
