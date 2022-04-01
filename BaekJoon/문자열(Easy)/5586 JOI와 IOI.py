import sys
lst = list(sys.stdin.readline().rstrip())

a = 0
b = 0
for i in range(len(lst)-2):
	if ''.join(lst[i: i+3]) == 'IOI':
		a += 1
	if ''.join(lst[i: i+3]) == 'JOI':
		b += 1

print(b)
print(a)