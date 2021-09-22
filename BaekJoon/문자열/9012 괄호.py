
T = int(input())
global tmp
tmp = 0
line = [[0 for _ in range(tmp)]for _ in range(T)]
for i in range(T):
	line[i] = list(input())
for i in range(T):
	leftCnt = 0
	rightCnt = 0
	stack = []
	if len(line[i]) % 2 != 0:
		print('NO')
		continue

	if line[i][0] == ')':
		print('NO')
		continue
	for j in line[i]:

		if len(stack) == 0 and j == ')':
			stack.append("~")
			continue
		if j == '(':
			leftCnt += 1
			stack.append(j)
		elif j == ')':
			stack.pop()
			rightCnt += 1
	if len(stack) != 0:
		print('NO')
		continue
	if leftCnt != rightCnt:
		print('NO')
		continue

	if len(stack) == 0:
		print('YES')
		continue

	continue

