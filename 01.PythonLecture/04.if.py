"""
흐름 제어 : if, elif, else
for 반복문
while 반복문
pass
예외 처리
range와 xrange
삼단 표현

if [조건식  > < .. True, False]:
    tab[space 4개]
"""
a = 10

if a == 10:#True
    print("a는 {}입니다.".format(a))

if a > 10:#False
    print("a > 10 입니다.")

if (a % 2) == 0:#True = 짝수
    print("a는 짝수 입니다.")

if (a % 2) != 0:#True = 홀수
    print("a는 홀수 입니다.")

if (a % 2) == 0:#True = 짝수
    print("a는 짝수 입니다.")
else :#False = 홀수
    print("a는 홀수 입니다.")


if (a % 3) == 0:
    print("나머지가 0 입니다.")
    print("나머지가 0 입니다.")
    print("나머지가 0 입니다.")
elif (a % 3) == 1:
    print("나머지가 1 입니다.")
elif (a % 3) == 2:
    print("나머지가 2 입니다.")
else:
    print("동작 오류")

# b <=저장= input() <= 키보드 입력
b = input()
print("입력값 {}".format(b))

# *문제 : 외부에서 값을 1개 받아서 짝수 홀수 여부를 출력
#input if elif else
input_value = int(input("값을 입력하시오. : "))

if (input_value % 2) == 0:
    print("{0}은 짝수입니다".format(input_value))
else:
    print("{0}은 홀수입니다.".format(input_value))

# *문제 : 0 ~ 100점 입력
# 90점이상 : A학점 입니다.
# 80점이상 : B학점 입니다.
# 70점이상 : C학점 입니다.
# 60점이상 : D학점 입니다.
# 60점미만 : F학점 입니다.
score = int(input("0~100점 입력 : "))
if (score >= 0) and (score <= 100) :
    if (score >= 90) :
        print("당신의 점수는 {} 점, 학점은 A 입니다.".format(score))
    elif (score >= 80) :
        print("당신의 점수는 {} 점, 학점은 B 입니다.".format(score))
    elif (score >= 70) :
        print("당신의 점수는 {} 점, 학점은 C 입니다.".format(score))
    elif (score >= 60) :
        print("당신의 점수는 {} 점, 학점은 D 입니다.".format(score))
    else :
        print("당신의 점수는 {} 점, 학점은 F 입니다.".format(score))

# *문제 - 값 3개 받습니다.
# a b c <= input()
# 가장 큰값, 가장 작은 값을 출력하세요.
a, b, c = 0,0,0
a = int(input("a값을 입력:"))
b = int(input("b값을 입력:"))
c = int(input("c값을 입력:"))

max, min = 0, 0 #초기화
# 1번째 솔루션 conditional expression (조건부 표현식)
max = a if a > b else b
max = c if c > max else max
min = a if a < b else b
min = c if c < min else min
print("최대값 : {}, 최소값 : {}".format(max,min))

# 2번째 솔루션
if a > b:
    max = a
    if max > c:
        pass
    else :
        max = c
else :
    max = b
    if max > c:
        pass
    else :
        max = c

if a > b:
    min = b
    if min < c:
        pass
    else :
        min = c
else :
    min = a
    if min < c:
        pass
    else :
        min = c


# 사칙연산 계산기
# a , b, oper <= + - * /

a = int(input("a값을 입력 : "))
oper = input("연산자 입력(+,-,*,/) : ")
b = int(input("b값을 입력 : "))

if oper == '+':
    print("{} + {} = {}".format(a,b,a+b))
elif oper == '-':
    print("{} - {} = {}".format(a,b,a-b))
elif oper == '*':
    print("{} * {} = {}".format(a,b,a*b))
elif oper == '/':
    print("{} / {} = {}".format(a,b,a/b))
else :
    print("입력이 잘못되었습니다.")


#조건문 (if, elif, else)
a = 30
if a == 10:
    print('hello world')
elif a<20 :
    print('good job 1')
else:
    print('else')

