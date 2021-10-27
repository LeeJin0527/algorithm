t = int(input())
for i in range(t):
	n = int(input())
	answer = []
	while True:
		if n <= 0:
			break
		k = n % 2
		n = n // 2
		answer.append(k)
	# print(answer)
	for i, v in enumerate(answer):
		if v == 1:
			print(i, end = ' ')
