
answer = input().split()
mula = int(answer[0])
cnt =1
while(1):
    if cnt == int(answer[2]):
        break
    
    mula *= int(answer[1])
    
    cnt += 1
print(mula)
