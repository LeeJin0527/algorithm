def solution(progresses, speeds):
	for i, v in enumerate(progresses):
		if ((100 - v) % speeds[i]) == 0:
			left.append((100 - v) // speeds[i])
		else:
			left.append((100 - v) // speeds[i]+1)
	# print(left)
	cnt = 0
	compare = left[0]
	for i in range(len(left)):
		if compare < left[i]:
			answer.append(cnt)
			compare = left[i]
			cnt = 0
		cnt += 1
	answer.append(cnt)
	return answer

answer = []
left = []
