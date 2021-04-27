temp =1
answer = input().split(" ")
for i in range(len(answer)):
    temp *= int(answer[i])
temp = format ((temp / 8 / 1024/ 1024), '.2f')
print(temp , "MB")
