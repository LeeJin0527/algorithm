n = int(input())
for i in range(n):
	line = list(input())
	accu = 0
	sum = 0
	for i in line:

		if i == 'O':
			sum += 1
			accu += sum
		else:
			sum = 0
			continue

	print(accu)



