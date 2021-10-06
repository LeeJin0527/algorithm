n = int(input())
charList = []
for i in range(n):
	charList.append(input())
# print(charList)
# 방문 했고 같은게 있는데 옆에 없다 -> 그룹 체커 아님
cnt = 0
flag = 0
for k, h in enumerate(charList):
	cnt += 1
	for i, v in enumerate(list(h)):
		# print('cnt~', cnt)
		if flag == -10000:
			flag = 0
			break
		for j in range(i+1, len(h)):
			if h.count(v) >= 2 and v == h[j]:
				# print(j)
				if h[j-1] != h[j]:
					cnt -= 1
					# print('cnt', cnt)
					flag = -10000
					break



print(cnt)
