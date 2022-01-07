import math
n = int(input())

def find_Prime(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, int(math.sqrt(x))+1):
		if x % i == 0:
			return False
	return True

def dfs(num, cnt):
	if cnt == n:
		print(num)
		return
	for i in [1, 3, 7, 9]:
		if find_Prime(10 * num + i):
			dfs(10 * num+i, cnt+1)

for num in [2, 3, 5, 7]:
	dfs(num, 1) 
