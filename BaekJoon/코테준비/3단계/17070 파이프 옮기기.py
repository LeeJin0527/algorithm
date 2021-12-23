n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
# [0, 1, 2 : 가로, 대각선, 세로], 행, 열
test = [[[0 for _ in range(n)] for j in range(n)] for _ in range(3)]
test[0][0][1] = 1
def dp():
	for i in range(n):
		for j in range(2, n):
			if box[i][j] == 1:
				continue
			test[0][i][j] = test[1][i][j-1] + test[0][i][j-1]
			if i == 0:
				continue
			test[2][i][j] = test[2][i-1][j] + test[1][i-1][j]
			if box[i-1][j] == 1 or box[i][j-1] == 1:
				continue
			test[1][i][j] = test[0][i-1][j-1]+ test[1][i-1][j-1] + test[2][i-1][j-1]
	return test[0][n-1][n-1] + test[1][n-1][n-1] + test[2][n-1][n-1]
print(dp()) 
