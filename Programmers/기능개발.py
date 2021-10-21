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

#new solution
def solution(progresses, speeds):
    progresses = [(100 - v) for i, v in enumerate(progresses)]
    for i, v in enumerate(progresses):
        if v % speeds[i] == 0:
            progresses[i] = v // speeds[i]
        else:
            progresses[i] = v // speeds[i] + 1
    print(progresses)
    compare = progresses[0]
    cnt = 0
    answer = []
    for i, v in enumerate (progresses):
        if compare >= v : 
            cnt += 1
        else:
            compare = v
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer
