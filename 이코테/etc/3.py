def recursive_function(i):
	if i == 10:
		return
	print(i, '번째 재귀 함수 에서 ', i+1, ' 번째 재귀 함수를 호출합니다.')
	recursive_function(i+1)
	print(i, '번째 재귀함수를 종료합니다')

recursive_function(1)