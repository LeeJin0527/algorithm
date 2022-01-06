import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(str, input().split()))
MinList = []
MaxList = []

k = 0
for i in range(10):
	if k == n+1:
		break
	MinList.append(i)
	MaxList.append(9-i)
	k += 1
for i in range(len(MaxList)-1):
	for j in range( len(MaxList)-1):
		if lst[j] == '<':
			if MaxList[j] > MaxList[j+1]:
				MaxList[j], MaxList[j+1] = MaxList[j+1], MaxList[j]
		else:
			if MaxList[j] < MaxList[j+1]:
				MaxList[j], MaxList[j+1] = MaxList[j+1], MaxList[j]
			else:
				continue

MaxList = map(str, MaxList)

for i in range(len(MinList)-1):
	for j in range(len(MinList)-1):
		if lst[j] == '>':
			if MinList[j] < MinList[j+1]:
				MinList[j], MinList[j+1] = MinList[j+1], MinList[j]
MinList = map(str, MinList)
print(''.join(MaxList))
print(''.join(MinList))