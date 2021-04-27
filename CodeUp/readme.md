codeup 기초 100제

# 1. sep(separation) 
 

영단어 그대로, 분리하여 출력한다. 다만 분리할 (갈라놓을 문자를 지정할 수 있다.) 이것을 구분자라고 한다.

예를 들어서 아래처럼 사용 할 수 있다.

print('S','E','P', sep='@')

출력 >>>>> S@E@P
S , E , P라는 문자열 사이에 @가 끼워넣어져 출력된다. 즉, 구분자는 @가 된다.

# 2. if 조건
if i % 2 == 0 and i !=0:
        print(' ', end ='')
    
    print(answer[i], end='')
if i != 0 조건 빼먹지 말기 (예외처리 중요)


# 3. conversion
 1) answer = int(input())

    print('%x' %answer)

 10진수를 16진수로 바꿀때는 뒤에 %연산자 써주는데 쉼표는 안쓴다!

 2) temp = int(answer, 16)
  
    print("%o" %temp)
    
  특정 진법으로 입력 받을 때는 같이 입력 받고 변환해주면 된다 
  
  3) answer = ord(input())
     print(answer)
     
  영문자를 입력 받아 10진수로 변환 할때는 ord
  
  4) answer = int(input())
     print(chr(answer))
   10진수 입력받아 영문자로 변환할때는 chr
   
  # 4. Decimal point
  print(format(float(answer),".2f"))
  formating ".2f" 
  반올림하여 소수 둘째짜리 까지 출력 
   






