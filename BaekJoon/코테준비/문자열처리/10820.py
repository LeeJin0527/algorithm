def box(lst):
	lowerCase , upperCase, number, space = 0, 0, 0, 0
	for i in lst:
		if 97 <= ord(i) < 123:
			lowerCase += 1
		elif 65 <= ord(i) < 91:
			upperCase += 1
		elif 48 <= ord(i) < 58:
			number += 1
		elif ord(i) == 32:
			space += 1
	return lowerCase, upperCase, number, space


while True:
	try:
		lst = list(input())
		answer = box(lst)
		for i in answer:
			print(i, end = ' ')
		print()
	except:
		break