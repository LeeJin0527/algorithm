import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

if len(lst) == 1:
	print(1)
	exit()

maxDp = [1] * (n)
minDp = [1] * (n)
for i in range(n):
	for j in range(i):
		if lst[i] > lst[j]:
			maxDp[i] = max(maxDp[j]+1, maxDp[i])



for i in range(len(lst)-1, -1, -1):
	for j in range(len(lst)-1, i-1, -1):
		# print(i, j)
		if lst[j] < lst[i]:
			minDp[i] = max(minDp[j] + 1, minDp[i])

result = 0
for i in range(n):

	try:
		resultMax = max(maxDp[:i+1])
	except:
		continue
	try:
		resultMin = max(minDp[i+1:])

		# print(maxDp[:i+1].index(resultMax), minDp[i+1:].index(resultMin))
		tmp = lst[i+1:]
		if lst[maxDp[:i+1].index(resultMax)] == tmp[minDp[i+1:].index(resultMin)]:
			resultMin -= 1
	except:
		continue
	result = max(result, resultMin + resultMax)

print(result)