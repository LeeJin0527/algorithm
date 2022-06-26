import sys
input = sys.stdin.readline
origin = input().rstrip()
popGroup = input().rstrip()
result = []
popGroupLength = len(popGroup)

remove = popGroup[-1]

for ori in origin:
	result.append(ori)
	if ori == remove and ''.join(result[-popGroupLength:]) == popGroup:
		del result[-popGroupLength:]

answer = ''.join(result)
if answer == "":
	print("FRULA")
else:
	print(answer)

