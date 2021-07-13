# n = input()
# x = ord(n[0])
# y = int(n[1])
# # print(type(x))
# # print(ord('a'))
# # print(ord('h'))
#
# dx = [2, 2, -2, -2, -1, -1, 1, 1]
# dy = [-1, 1, 1, -1, 2, -2, 2, -2]
# count = 0
# for i in range(8):
# 	count += 1
# 	if (dx[i] + x) < 97 or (dx[i] + x) > 104 or (dy[i] + y) < 1 or (dy[i]+ y) > 8 :
# 		count -=1
# 		continue
#
#
# print(count)

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 나이트가 이동할 수 있는 8가지 방향 정의
steps =[(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
for step in steps:
	# 이동하고자 하는 위치 확인
	next_row = row + step[0]
	next_column = column + step[1]

	if next_row >=1 and next_row <= 8 and next_column >=1 or next_column<=8 :
		result += 1
print(result)