answer = [0 for _ in range(26)]
lst = list(input())
for i, v in enumerate(lst):
	answer[(ord(v) - ord('a'))] += 1
for i in answer:
	print(i, end = ' ')