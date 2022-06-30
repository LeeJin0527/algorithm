import sys
input = sys.stdin.readline
n, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def matrix_pow(A, B):
	if B == 1:
		return A
	elif B % 2 == 0:
		temp = matrix_pow(A, B // 2)
		return matrix_mul(temp, temp)
	else:
		temp = matrix_pow(A, B -1)
		return matrix_mul(temp, A)

def matrix_mul(mat_a, mat_b):
	mat_c = [[0] * len(mat_a) for _ in range(len(mat_a))]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				mat_c[i][j] += mat_a[i][k] * mat_b[k][j]
			mat_c[i][j] %= 1000
	return mat_c


result = matrix_pow(lst, b)
for i in result:
	for j in i:
		print(j % 1000, end = ' ')
	print()
