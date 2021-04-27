answer = input().split()
suma = int(answer[0])
cnt =1
while(1):
    if cnt == int(answer[2]):
        break
    
    suma += int(answer[1])
    
    cnt += 1
print(suma)
