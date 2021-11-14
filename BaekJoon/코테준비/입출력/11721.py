lst = list(input())
for i in range(0, len(lst), 10):
	answer = ''.join(lst[i:i+10])
	print(answer)
