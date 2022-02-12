
lst = []
for _ in range(5):
	lst.append(list(input()))
m = 0
for i in lst:
	if m < len(i):
		m = len(i)

answer = ''
for i in range(m):
	for j in range(5):
		try:
			answer += lst[j][i]
		except:
			continue
print(answer)