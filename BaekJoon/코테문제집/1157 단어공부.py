import sys
answer = sys.stdin.readline().rstrip().upper()
lst = [0] * 26
for i in answer:
	lst[ord(i)-65] += 1

tmp = lst.count(max(lst))
if tmp >= 2:
	print('?')
else:
	result = lst.index(max(lst))
	print(chr(result + 65))