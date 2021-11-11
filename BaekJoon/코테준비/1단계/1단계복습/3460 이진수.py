t = int(input())
for i in range(t):
	target = int(input())
	answer = []
	while True:
		answer.append(target % 2)
		if target == 1:
			break
		target = target // 2

	for i, v in enumerate(answer):
		if v == 1:
			print(i, end = ' ')



