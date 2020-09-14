def answer():
    import sys
    tmp=original=int(sys.stdin.readline())

    count=0
    while True:
        a = tmp//10
        b = tmp%10
        sum = a + b
        count +=  1
        tmp=int(str(tmp%10)+str(tmp%10))

        if(tmp==original):
            break
    print(count)



if __name__ =='__main__':
    answer()
    '''문제 분석
    처음에 tmp 안쓰고 새로운 숫자 생성할 때 new로 갱신하려고 했는데 시간 초과가 뜸 근데 pycharm에서는 답이 잘 나옴
    위의 방법을 쓰면 시간초과가 나는 이유는
    original 값이 계속 갱신되기 때문인 것 같은데 처음에 original을 전역변수로 설정해 둬서 답이 나온 듯
    애초에 original 값과 비교할게 필요했기 때문에 새로운 변수인 tmp에 넣고 시작하는게 좋았을 듯
    그리고 int(str+str)가능한거 레전드인듯 
    원래 생각했던 방식은 문자열->숫자->문자열 로 번거로운 방식인데 각 자리수를 직접 구하니 문제풀기 훨씬 수월했음 
    휴~ 아직 갈 길이 먼 듯
    
    '''