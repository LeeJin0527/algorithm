n, k = map(int, input().split())
line = []
for i in range(n):
	line.append(int(input()))
line.sort(reverse=True)
answer = 0
result = k
for i in line:
	if result >= i:
		answer += result // i
		result = result % i

	if result == 0:
		break


print(answer)
# print(result)


