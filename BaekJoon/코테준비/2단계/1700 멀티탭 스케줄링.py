n, k = map(int, input().split())
lst = list(map(int, input().split()))

# print(answer)
answer = []
cnt = 0
first = 0
for i in range(len(lst)):
	# lst[i] 가 answer 에 있으면 continue
	# lst[i]가 없으면 그 다음 요소부터 이루어진 배열에서 answer이 가장 처음 언제 나오는지 확인 후 늦게 나오는것과 swap cnt += 1
	if first < n:
		if lst[i] not in answer:
			answer.append(lst[i])
			first += 1
		else:
			continue
	else:
		if lst[i] in answer:
			continue
		tmp = lst[i+1:]
		tmp = list(map(str, tmp))
		tmp = ''.join(tmp)
		# print(tmp)
		comp = []

		for j in answer:
			mid = tmp.find(str(j))
			if mid == -1:
				mid = 101
			comp.append([mid, j])
		# print('cc',comp)
		comp.sort()
		change = comp[-1][1]
		tmp = list(map(int, tmp))
		try:
			insert = answer.index(change)
			# print(insert)
			answer[insert] = lst[i]
			cnt += 1
		except:
			answer[0] = lst[i]
			cnt += 1
print(cnt)
 
