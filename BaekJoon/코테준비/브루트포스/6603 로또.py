from itertools import combinations
while True:
	lst = list(map(int, input().split()))
	answer = lst[1:]
	if lst[0] == 0:
		break

	for i in list(combinations(answer, 6)):
		for j in i:
			print(j, end = ' ')
		print()
	print()