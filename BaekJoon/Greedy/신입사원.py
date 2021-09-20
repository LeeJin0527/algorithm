t = int(input())
global tmp
tmp = 0
answer = [[0 for _ in range(tmp)] for row in range(t)]

for i in range(t):
	tmp = int(input())
	for j in range(tmp):
		answer[i].append(list(map(int,input().split())))

for i in range(t):
	answer[i] = sorted(answer[i], key = lambda x : x[1])
	# print('answer[i]', answer[i])
	# print('answer[i]',answer[i])
	# print(len(answer[i]))
	cnt = 1
	k = 1
	j = 0
	while True:

		if answer[i][j][0] >= answer[i][k][0]:
			cnt += 1
			# print("~")
			if ( k - j) > 1:
				j += (k-j)-1
			j += 1
			k += 1

		else:
			k += 1
			# print(j, k )

		if k > (len(answer[i]) -1):
			break


	print(cnt)

