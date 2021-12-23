from itertools import combinations
n, k = map(int, input().split())
origin = ['a', 'n', 't', 'i', 'c']
candiInt = [0 for _ in range(n)]
for i in range(n):
	start = list(input())[4:-4]
	for j in start:
		candiInt[i] |= 1 << (ord(j) - 97)


alpha = []
for i in range(97, 123):
	if chr(i) not in origin:
		alpha.append(chr(i))

answer = 0

if k-5 < 0:
	print(0)
	exit()
for i in list(combinations(alpha, k-5)):
	tmp = 0
	for j in list(i):
		tmp |= 1 << (ord(j) - 97)
	for j in origin:
		tmp |= 1 << (ord(j) -97)
	#tmp 에 candi가  몇개나 들어가는지 확인
	cnt = 0
	for k in range(len(candiInt)):
		if candiInt[k] & tmp == candiInt[k]:
			cnt += 1
	answer = max(answer, cnt)

print(answer)






