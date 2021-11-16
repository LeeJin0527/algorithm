n, m = map(int, input().split())
k = int(input())
lst = list(map(int, input().split()))
s = len(lst)
tmp = 0
for i in range(s):
	tmp += lst[i] * n ** (s-i-1)
result = []
while True:
	result.append(tmp % m)
	tmp = tmp // m
	if tmp < m:
		break
result.reverse()
if tmp != 0:
	answer =[tmp] + result
else:
	answer = result

for i in answer:
	print(i, end = ' ')
