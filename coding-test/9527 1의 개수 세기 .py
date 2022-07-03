import sys
input = sys.stdin.readline
a, b = map(int, input().split())
psum = [0] * 60
for i in range(1, 60):
	psum[i] = 2 ** (i-1) + 2 * psum[i-1]

def check(num):
	count = 0
	decToBin = bin(num)[2:]
	length = len(decToBin)
	for i in range(length):
		if decToBin[i] == '1':
			pow = length - i - 1
			count += psum[pow]
			count += num - (2 ** pow) + 1
			num = num - 2 ** pow
	return count

print(check(b) - check(a-1))
