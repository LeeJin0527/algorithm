import sys
lst = list(input().split())
common = lst[0]

compare = lst[1:]
compare = [item.replace(",", "") for item in compare]
compare = [item.replace(";", "") for item in compare]


for i in compare:
	if all(65 <= ord(j) <= 90 or 97<=ord(j)<=122 for j in list(i)):
			print(common, i+";")
	else:
		for j, v in enumerate(i):
			if ord(v) == 91 or ord(v) == 93 or ord(v)==42 or ord(v) ==38:
				break
		last = i[:j]+";"
		tmp = i[j:]
		tmp = tmp[::-1]
		tmp = [item.replace("[", "-") for item in tmp]
		tmp = [item.replace("]", "[") for item in tmp]
		tmp = [item.replace("-", "]") for item in tmp]
		print(common+''.join(tmp),last)
