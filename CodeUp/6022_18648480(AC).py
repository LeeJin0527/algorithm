answer = input()
for i in range(len(answer)):
    if i % 2 == 0 and i !=0:
        print(' ', end ='')
    
    print(answer[i], end='')
