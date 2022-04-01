import sys
while True:
	lst = sys.stdin.readline().rstrip('\n')

	if lst == '***':
		exit()
	else:
		lst = list(lst)
		lst.reverse()
		print(''.join(lst))