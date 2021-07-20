def sequential_search(n, target, array):
	data = []
	for i in range(n):
		if array[i] == target:
			data.append(i+1)
	return data

print("생성할 원소의 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸 으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))