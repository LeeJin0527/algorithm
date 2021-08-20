def solution(food_times, k):

	if sum(food_times) <= k:
		return -1

	data = []
	sublist = []


	for i in range(len(food_times)):
		data.append((food_times[i], i+1))
	left = len(data)
	data.sort()
	# print(data)
	pretime = 0

	for i in range(len(data)):

		diff = data[i][0] - pretime
		if diff != 0:
			tmp = diff * left
			# print(tmp)

			if tmp <= k:
				k -= tmp
				pretime = data[i][0]

			else:
				k %= left
				sublist = data[i:]
				sublist.sort(key = lambda x:x[1])

				# print(sublist[k][1])
				return sublist[k][1]

		left -= 1



solution([3, 1, 2], 5)
