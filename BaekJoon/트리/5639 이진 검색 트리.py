import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
lst = []
while True:
	try:
		lst.append(int(input()))
	except:
		break

def dfs(arr):

	if len(arr) == 1:
		print(arr[0])
		return
	if len(arr) < 1:
		return
	root = arr[0]
	tmp = len(arr)
	for i in range(1, len(arr)):
		if root < arr[i]:
			tmp = i
			break

	dfs(arr[1:tmp])
	dfs(arr[tmp:])
	print(root)

dfs(lst)