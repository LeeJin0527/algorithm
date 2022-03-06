import sys
input= sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
left = [1] * n
for i in range(len(lst)):
	for j in range(i):
		if lst[i] > lst[j]:
			left[i] = max(left[i], left[j] + 1)
# print(left)
right = [1] * n
compare = list(reversed(lst))
for i in range(len(lst)):
	for j in range(i):
		if compare[i] > compare[j]:
			right[i] = max(right[i], right[j] + 1)
right.reverse()
# print(right)
answer = 0
if len(lst) == 1:
	print(1)
	exit()
for i in range(n+1):

	x = left[:i]
	try:
		resultX = max(x)
	except:
		continue

	y = right[i:]
	try:
		resultY = max(y)
	except:
		continue

	if x[x.index(resultX)] == y[y.index(resultY)]:
		answer = max(answer,resultX + resultY-1 )

	else:
		answer = max(answer,resultX + resultY)
print(answer)
