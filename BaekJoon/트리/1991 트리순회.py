import sys
input = sys.stdin.readline
n = int(input())
trees = {}
for _ in range(n):
	root, left, right = list(sys.stdin.readline().rstrip().split())
	trees[root] = [left, right]

def preorder(root):
	if root != '.':
		print(root, end ='')
		preorder(trees[root][0])
		preorder(trees[root][1])

def inorder(root):
	if root != '.':
		inorder(trees[root][0])
		print(root, end ='')
		inorder(trees[root][1])

def postorder(root):
	if root != '.':
		postorder(trees[root][0])
		postorder(trees[root][1])
		print(root, end ='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
