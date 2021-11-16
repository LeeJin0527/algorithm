answer = [-1 for _ in range(26)]
lst = list(input())
for i, v in enumerate(lst):
	if answer[ord(v)- ord('a')] != -1:
		continue
	answer[(ord(v) - ord('a'))] = i

for i in answer:
	print(i, end = ' ')