from itertools import combinations
lst = []
for i in range(9):
	lst.append(int(input()))

for i in list(combinations(lst, 7)):
	if(sum(i)) == 100:
		answer = list(i)
		break

answer.sort()

for i in answer:
	print(i)