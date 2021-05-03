a =  input().split('-')
suma =0 
tmp =[]
answer = -1

for i, v  in enumerate(a):
    if i == 0 :
        if '+' in v:
            v = v.split('+')
            for i in v:
                suma += int(i)
                answer = int(suma)
        else:
            answer = int(v)
        
    else:
        suma = 0
        if '+' in v:
            v = v.split('+')
            for i in v:
                suma += int(i)
                #answer = suma
            #print(answer)
            answer -= suma
            #print(answer)
            
        else:
            answer -=int(v)
print(answer)
