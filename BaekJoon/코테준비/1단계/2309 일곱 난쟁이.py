from itertools import combinations
answer = []
for i in range(9):
	m = int(input())
	answer.append(m)
answer = sorted(answer)
# print(answer)
for i in list(combinations(answer, 7)):
	if sum(i) == 100:
		for j in i:
			print(j)
		break