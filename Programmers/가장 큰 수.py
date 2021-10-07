def solution(numbers):
	numbers = list(map(str, numbers))
	store = [[] for i in range(10)]
	for i, v in enumerate(numbers):
		store[int(v[0])].append(v)
	store.reverse()
	# print(store)
	for kkk, i in enumerate(store):
		if i :
			if len(i)>=2:
				i.sort(key = lambda x : x *3, reverse = True)
				store[kkk] = i
	# print(store)
	answer = ''
	cnt = 0
	for i in store:
		if i:
			for j in i:
				answer += j
	# print(answer)
	for i in answer:
		if i == '0':
			cnt += 1
	if cnt == len(answer):
		answer='0'


	return answer
print(solution([0, 0, 0]))