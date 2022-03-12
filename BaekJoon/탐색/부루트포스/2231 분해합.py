import sys
input = sys.stdin.readline
n = int(input())

for i in range(1, n+1):
	answer = 0
	answer += i
	for j in range(len(str(i))):
		answer += int(str(i)[j])

	if answer == n:
		print(i)
		exit()
print(0)