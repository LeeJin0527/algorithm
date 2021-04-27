answer = input().split()
temp = int(answer[0])
cnt =1
while(1):
    if cnt == int(answer[3]):
        break
    
    temp = temp *int(answer[1]) + int(answer[2])
    
    cnt += 1
print(temp)
