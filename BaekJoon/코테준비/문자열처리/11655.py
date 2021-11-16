lst = list(input())
answer = []
for i in lst:
	if 48 <= ord(i) < 58:
		answer.append(i)
	elif ord(i) == 32:
		answer.append(i)
	elif 65 <= ord(i) < 91:
		if ord(i) + 13 > 90:
			answer.append(chr((ord(i) + 13) - 26))
		else:
			answer.append(chr(ord(i)+ 13))
	elif 97 <= ord(i) <123:
		if ord(i) + 13 > 122:
			answer.append(chr((ord(i)+13)-26))
		else:
			answer.append(chr((ord(i) + 13)))
for i in answer:
	print(i, end = '')
