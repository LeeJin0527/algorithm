from itertools import permutations

def solution(k, dungeons):
	lst = [i for i in range(len(dungeons))]
	maxValue = 0
	for i in list(permutations(lst, len(dungeons))):
		compare = k
		lst = []
		for j in i:
			if dungeons[j][0] <= compare:
				compare = compare - dungeons[j][1]
				lst.append(compare)

		maxValue = max(maxValue, len(lst))
	answer = maxValue

	return answer