# 성냥개비 개수로 만들수 있는 수
import time
from itertools import combinations_with_replacement
#조합 배열 생성
compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
comAnswer = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 0: 6, 6: 6, 9: 6, 7: 3, 8: 7}
answer = {2: 1, 5: 2, 4: 4, 6: 0, 3: 7, 7: 8}
combination = [2, 3, 4, 5, 6, 7]
# 입력
tmps = []
# 입력
n = int(input())
for i in range(n):
	tmps.append(int(input()))

for tmp in tmps:
	maxTmp = tmp
	if tmp <= 7:
		if tmp == 6:
			Min = 6
		else:
			Min = answer[tmp]
	else:
		state = 0
		if tmp % 7 == 0:
			state = tmp // 7 -1
		else:
			state = tmp // 7
		ret = -1
		for i, v in enumerate(compare):
			if ret == -2:
				break
			last = []
			first = []
			first.append(str(v))
			for j in combinations_with_replacement(combination, state):
				if (tmp - comAnswer[v]) == sum(j):
					# print(j)
					last.append(list(j))

					ret = -2

				else:
					continue
		last = [[answer[k] for j, k in enumerate(v)] for i, v in enumerate(last)]
		last = [[str(k) for j, k in enumerate(v)] for i, v in enumerate(last)]
		last = [''.join(v) for i, v in enumerate(last)]
		MinList = []
		Min = ''
		first = len(last) * first
		for i in range(len(first)):
			Min = first[i] + last[i]
			MinList.append(Min)
		last = list(map(int, MinList))
		last = min(last)

	# # 앞자리가 0으로 차는 경우는 6으로 바꿔줌
	maxList = []
	if maxTmp % 2 == 0:
		maxList = [2 for i in range(maxTmp //2)]
	else:
		if (maxTmp - 3) % 2 == 0:
			maxList = [2 for i in range((maxTmp - 3) // 2)]
			maxList.append(3)
	maxList = sorted(maxList, reverse=True)
	maxList = [answer[v] for i, v in enumerate(maxList)]
	maxList = [str(v) for i, v in enumerate(maxList)]
	Max = (''.join(maxList))
	Max = int(Max)
	print(Min, Max)
