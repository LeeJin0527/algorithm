import sys
import itertools as it
input = sys.stdin.readline
n, m = map(int, input().split())
alphaList = {'A' : 3, 'B' : 2, 'C' : 1, 'D': 2, 'E' : 4, 'F' : 3,
             'G' : 1, 'H' : 3, 'I' : 1, 'J' : 1, 'K' : 3, 'L' : 1, 'M' : 3, 'N' : 2, 'O' : 1, 'P' : 2,
             'Q' : 2, 'R': 2, 'S' : 1, 'T' : 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1 }
start, second = input().split()
start = list(start)
second = list(second)
store = list(it.chain(*zip(start,second)))
if n > m:
	store.extend(start[-(n-m):])
elif n < m:
	store.extend(second[-(m-n):])
for i, v in enumerate(store):
	store[i] = alphaList[v]

while True:

	lst = [0] * (len(store)-1)
	if len(lst) == 1:
		break
	for i in range(len(lst)):
		tmp = store[i]+store[i+1]
		if tmp >= 10:
			lst[i] = int(str(tmp)[-1])
		else:
			lst[i] = tmp
	last = lst
	store = lst

if last[0] == 0:
	print(str(last[1]) + "%")
else:
	print(str(last[0]) + str(last[1]) + "%")
