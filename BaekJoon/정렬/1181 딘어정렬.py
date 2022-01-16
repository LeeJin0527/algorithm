n = int(input())
lst = []
for i in range(n):
	lst.append(input())
lst = set(lst)
answer = list(lst)
answer.sort(key=lambda x:(len(x), x))
for i in answer:
	print(i)