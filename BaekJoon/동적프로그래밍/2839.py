N = int(input())
vinyl = 0
sugar = N
while(True):

	if sugar % 5 == 0 :
		vinyl += sugar // 5
		break

	elif sugar < 3:
		#sugar = 1 vinyl = 1
		vinyl = -1
		break

	else:
		sugar = sugar - 3
		vinyl += 1

print(vinyl)




