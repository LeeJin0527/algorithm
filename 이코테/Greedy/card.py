# N, M = map(int, input().split())
# tmp =[]
# for i in range(N):
# 	data = list(map(int, input().split()))
# 	data.sort()
# 	tmp.append(data[0])
#
# tmp.sort(reverse = True)
# print(tmp[0])

N, M = map(int, input().split())
result = 0
for i in range(N):
	data = list(map(int, input().split()))
	min_value = 10001
	for j in data:
		min_value = min(j, min_value)

	result = max(result, min_value)
print(result)
