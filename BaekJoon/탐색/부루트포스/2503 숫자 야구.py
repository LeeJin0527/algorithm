import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
	a, b, c = map(int, input().split())
	lst.append([a, b, c])
cnt = 0
for i in range(100, 1000):
	# i = 100

	compare = list(str(i))
	if len(set(compare)) != 3:
		continue
	if '0' in compare:
		continue
	answer = 0
	for j in lst:
		# j = 123 356 327 489

		tmp = list(str(j[0]))
		# print(compare, tmp)
		strike = j[1]
		ball = j[2]

		aa = 0
		bb = 0
		for k in range(3):
			if compare[k] == tmp[k]:
				aa += 1

			if compare[k] != tmp[k] and str(compare[k]) in tmp:
				# print(str(compare[k]))
				bb += 1
		# print(aa, strike, bb, ball)
		if aa == strike and bb == ball:
			answer += 1

	if answer == n:

		cnt += 1

print(cnt)
