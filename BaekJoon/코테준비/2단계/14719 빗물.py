h, w = map(int, input().split())
lst = []
for i in input().split():
	lst.append(int(i))
answer = 0
for i in range(1, len(lst)-1):
	left = max(lst[:i])
	right = max(lst[i+1:])
	block = min(left, right)
	if lst[i] < block:
		answer += block - lst[i]
print(answer)

 
