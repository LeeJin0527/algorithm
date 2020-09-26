'''문제분석:
d(18)=28나와서 헤맴
 n=n//10 이렇게 하니까 답이 잘 나옴
 '''
def d(n):
    ret = n
    while(n!=0):
        ret=ret+n%10 #26
        #26+1=27

        n=n//10 #1

    return int(ret)

if __name__=='__main__':
    #print(d(18))
    arr=[0]*10001
    for i in range(10000):
        if(d(i)<10000):
            arr[int(d(i))]=1


    for i in range(10000):
        if (arr[i]==0):
            print(i)




