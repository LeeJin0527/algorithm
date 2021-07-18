n, k= map(int, input().split())

goal = list(map(int, input().split()))
tmp = list(map(int, input().split()))

goal.sort()
tmp.sort(reverse = True)

# print(goal)
# print(tmp)

for i in range(k):
	if goal[i] < tmp[i]:
		goal[i], tmp[i]  = tmp[i], goal [i]
	else:
		break

# print(goal)
# print(tmp)
sum  = 0
for i in goal :
	sum += i
print(sum)
