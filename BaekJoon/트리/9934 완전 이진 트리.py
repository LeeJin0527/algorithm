import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
trees = [[]  for _ in range(n)]
def makeTree(arr, i):
	root = len(arr) // 2
	trees[i].append(arr[root])
	if len(arr) == 1:
		return
	makeTree(arr[:root], i+1)
	makeTree(arr[root+1:], i+1)
makeTree(lst, 0)
for i in trees:
	print(*i)