import sys
import math
lst = list(sys.stdin.readline().rstrip())
answer = 0
for i in lst:
	if 97 <= ord(i) <= 122:
		answer += ord(i) - 97 + 1
	elif 65 <= ord(i) <= 90:
		answer += ord(i) - 65 + 1

for i in range(2, int(math.sqrt(answer))+1):
	if answer % i == 0:
		print('It is not a prime word.')
		exit()
print('It is a prime word.')

