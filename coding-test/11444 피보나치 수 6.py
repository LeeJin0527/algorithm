import sys
input = sys.stdin.readline
n = int(input())
lst = [[1, 1], [1, 0]]
def mat_mul(mat_a, mat_b):
	mat_c = [[0] * len(mat_a) for _ in range(len(mat_a))]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				mat_c[i][j] += (mat_a[i][k] * mat_b[k][j]) % 1000000007
	return mat_c

def mat_pow(A, B):
	if B == 1:
		return A
	elif B % 2 == 0:
		temp = mat_pow(A, B // 2)
		return mat_mul(temp, temp)
	else:
		temp = mat_pow(A, B-1)
		return mat_mul(temp, A)


result = mat_pow(lst, n)
print(result[0][1] % 1000000007)
