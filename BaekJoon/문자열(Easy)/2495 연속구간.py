import sys

for _ in range(3):
	lst = list(sys.stdin.readline().rstrip())

	answer = [0] * len(lst)
	for i in range(len(lst)):
		for j in range(i, len(lst)):
			if lst[i] == lst[j]:
				answer[i] += 1
			else:
				break
	print(max(answer))