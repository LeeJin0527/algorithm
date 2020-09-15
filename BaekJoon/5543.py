
def answer(number):
    import sys
    list_a=[]
    for i in range(5):
        a=sys.stdin.readline()
        list_a.append(int(a))
    #print(list(map(int,list_a)))

    min=list_a[0]
    for j in range(3):
        if (int(min) > int(list_a[j])):
            min = list_a[j]

    #print(min)

    min2=list_a[3]
    for k in range(3,5):
        if (int(min2) > int(list_a[k])):
            min2 = int(list_a[k])

    #print(min2)

    print(int(min)+int(min2)-50)



if __name__ =='__main__':
    answer(int)


'''
이어서 받을수 있구나.. 변수 같으면,, ㅜ 개고생했네 
그리고 min 내장함수니 이용하장 다음부턴~
def answer(number):
    import sys
    a=2000
    c=2000

    for i in range(3):
        b=int(sys.stdin.readline())
        a=min(a,b)
    #print(list(map(int,list_a)))


    for i in range(2):
        b = int(sys.stdin.readline())
        c=min(c,b)

    #print(min)

    print(a+c-50)

'''