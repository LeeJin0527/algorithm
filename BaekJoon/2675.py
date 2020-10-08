'''문제분석:
end='' 의 마지막 줄 처리를 잘해야함
print((int(cha[0]) * cha[1][j]),end='')로 마지막 입력 처리를 안해주면 다음 입력에 지장을 주기 때문에 처리를 해줘야 한다
 for j in range(len(cha[1])-1):
            print((int(cha[0]) * cha[1][j]),end='')
        print((int(cha[0]) * cha[1][-1])) 즉 이렇게 처리해줘야 다음 입력을 무사히 받을 수 있따!!
'''

# '''2675 문제: 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
#
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
#
# 출력
# 각 테스트 케이스에 대해 P를 출력한다.
#
# 예제 입력 1
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1
# AAABBBCCC
# /////HHHHHTTTTTPPPPP'''


def answer():
    import sys
    num=sys.stdin.readline()

    for i in range(int(num)):

        cha=sys.stdin.readline().split()
        for j in range(len(cha[1])-1):
            print((int(cha[0]) * cha[1][j]),end='')
        print((int(cha[0]) * cha[1][-1]))








        # print((int(cha[0]))*list(cha[1][0]))
        # print((int(cha[0]))*list(cha[1][1]))
        # print((int(cha[0]))*list(cha[1][2]))




if __name__ =="__main__":
    answer()