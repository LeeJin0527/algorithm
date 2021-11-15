import sys
input = sys.stdin.readline
n = int(input())
stk = []
for i in range(n):
	tmp = input().split()
	if tmp[0] == 'push':
		stk.append(int(tmp[1]))
	elif tmp[0] == 'top':
		try:
			print(stk[-1])
		except:
			print(-1)
	elif tmp[0] == 'pop':
		try:
			x = stk.pop()
			print(x)
		except:
			print(-1)
	elif tmp[0] == 'size':
		print(len(stk))

	elif tmp[0] == 'empty':
		if len(stk) == 0 :
			print(1)
		else:
			print(0)


