def rotate_a_matrix_by_90_degree(a):
	row_length = len(a)
	# print(row_length)
	column_length = len(a[0])
	# print(column_length)
	res = [[0] * row_length for _ in range(column_length)]
	# print(res)

	for r in range(row_length):
		for c in range(column_length):
			res[c][row_length -1 -r] = a[r][c]
	return res

a = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))