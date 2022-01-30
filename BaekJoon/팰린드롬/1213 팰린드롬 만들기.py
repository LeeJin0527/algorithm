import sys
from collections import defaultdict
input = sys.stdin.readline
lst = list(sys.stdin.readline().rstrip())
lst.sort()
count = defaultdict(int)
for i in lst:
	count[i] += 1
exitCnt = 0
answer = []
mid = ''
for i in count:
	if count[i] % 2 == 1:
		exitCnt += 1
		mid = i
		# count[i] -= 1
	if exitCnt >= 2:
		print("I'm Sorry Hansoo")
		exit()
	for j in range(count[i] // 2):
		answer.append(i)
end = list(reversed(answer))
if mid == '':
	print(''.join(answer) + ''.join(end))
else:
	print(''.join(answer) +mid + ''.join(end))











