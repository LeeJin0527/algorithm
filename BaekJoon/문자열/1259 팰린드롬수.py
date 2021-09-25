import math

while True:
	n = 0

	n = input()
	if n == '0':
		break

	cnt = 0
	if len(n) == 1:
		print('yes')
		continue
	for i in range(len(n) // 2):
		if n[i] == n[len(n) - 1 - i]:
			cnt += 1

		else:
			print('no')
			break


		if cnt == len(n) // 2:
			print('yes')
			continue

