n = input()
cnt = 0

if len(n) == 1:
	print(1)


for i in range(len(n) // 2):


	if n[i] == n[len(n)-1-i]:
		cnt += 1
	else:
		print(0)
		break

	if cnt == len(n) // 2:
		print(1)


