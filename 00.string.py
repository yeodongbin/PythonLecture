################ 문자열
# 문자열은 기본적으로 리스트랑 비슷한 형식을 갖는다
#ll = ['조','영','학','','전''''']
ss = '조영학 전예지 행복해라'
print(ss[0])
print(ss[0:5])
# 리스트와 동일하게 첨자를 이용해 자리값 출력

ss = '조영학'+' 전예지'+' 행복해라'
print(ss)
# 더하기 연산
ss = '행복해라 ' * 4
print(ss)
# 곱하기 연산
print(len(ss))
# len() 함수를 이용해서 문자열의 길이를 출력

#### 문자열 각 문자 뒤에 다른 문자 입력 for문
ss = '락초이김기범사귀지마라'

sslen = len(ss)
for i in range(0, sslen) :
    print(ss[i]+'$' , end='')
print('')


# 문자열 사이값 출력
print("안녕","하세요", sep="!") 

a = '010'
b = '1577'
c = '8282'
print(a,b,c,sep='-')



##### 문자열 입력 받고, 꺼꾸로 출력
inss, outss = '',''
count, i = 0,0

inss = input("문자열을 입력하세요: ")
count = len(inss)

for i in range(0, count) :
    outss += inss[count-(i+1)]

print("내용 거꾸로 출력 -> %s" % outss)
print('')




# Quiz) while 문으로 바꿔서 만들어 보자

############### 문자열관련 함수  ################
ss = "asdf AwefDF ㅁ;ㅣ나어리;ㅁ ^^"
print(ss.upper())
# upper : 대문자로 바꿔주는 함수
print(ss.lower())
# lower : 소문자로 바꿔주는 함수
print(ss.swapcase())
# swapcase : 대문자와 소문자를 서로 바꿔주는 함수
print(ss.title())
# 가장 앞 한글자를 대문자로 바꿔주는 함수
## 4가지 함수는 영어!!! 에서만 작용한다.

ss = '파이썬 공부는 즐겁습니다. 개소리,, 물론 모든 공부가 다 재미있지는 않죠. ^^'
print(ss.count('공부'), ss.find('공부'), ss.rfind('공부'), ss.find('없다'))
# count : 해당 단어 갯수 , find : 해당 단어 위치, rfind : 오른쪽부터 해당단어 위치
# cf) 해당단어를 찾을 수 없을 때 -1 값을 출력
# ('단어', 시작값)

print(ss.index('공부'), ss.rindex('공부'), ss.index('공부',5))
# find랑 동일하게 해당 단어가 있는 위치를 출력
# index는 찾는 단어가 없을 때 프로그램 오류가 발생
# ('단어', 시작값)

print(ss.startswith('파이썬'), ss.startswith('파이썬',10), ss.endswith("^^"))
# startswith : 해당 단어로 시작하면 True 아니면 false
# endswith : 해당 단어로 끝나면 True 아니면 false
# ("단어", 시작값)


### 문자열이 괄호로 감싸져 있지 않으면 감싸주는 프로그램
ss = input("문자열 입력 : ")
print("출력 문자열 ==>", end='')

if ss.startswith('(') == False :
    print("(", end='')
print(ss, end='')

if ss.endswith(')') == False :
    print(")", end='')
print('')

# Quiz) while => '끝' 문자 입력하지 않으면 끝나지 않게



ss = '  파   이   썬   '
print(ss.strip())
# 앞뒤의 공백을 삭제, 중간 띄어쓰기는 유지
print(ss.rstrip())
# 오른쪽 공백 삭제
print(ss.lstrip())
# 왼쪽 공백 삭제

ss = '----파----이----썬----'
print(ss.strip('-'))
# 공백 뿐 아니라, 특수 문자도 삭제, 중간 문자는 유지
print(ss.rstrip('-'))
print(ss.lstrip('-'))


### 문자열에 모든 공백 제거하는 프로그램
inss = "    한글    python    최낙준    "
outss = ""

for i in range(0, len(inss)) :
    if inss[i] != ' ' :
        outss += inss[i]

print('원래 문자열 =>'+ '['+ inss +']')
print('공백 제서 =>'+ '['+ outss +']')

# Quiz ) <<<파<<<이>>>썬>>> -> 파이썬 으로 출력되게 ㄱㄱ



##### 문자열 내용 변경
ss = "열심히 파이썬을 공부중~~~"
print(ss.replace("파이썬", "python"))
print(ss)
# replce :  대체, 해당 단어를 설정한 단어로 교체
# 임시로 바뀜
# 문자열 자체를 바꾸는게 아니라 출력문만 변경


# 1. 문자열에 문자를 대체하는 프로그램
ss = input("문자열 입력 : ")
print("출력할 문자열 = " , end='')

for i in range(0, len(ss)) :
    if ss[i] != 'o' :
        print(ss[i], end='')
    else :
        print('$', end = '')
print('')


# 2. python 에서 제공해 주는 함수 사용
ss = input("문자열 입력 : ")
print("출력할 문자열 = ", ss.replace("o", '$'))



##### 문자열 분리, 결합
ss = 'Python을 열심히 공부 중'
print(ss.split())
# 띄어쓰기를 기준으로 리스트의 항목으로 분리 시켜 출력

ss = "김연세, 전예지, 조영학, 문선종, 함승필"
ss = '010-6733-1864'
print(ss.split(','))
# split('기준') 특정문자를 기준으로 삼을 수 있음

ss = "김연세\n전예지\n조영학\n문선종\n함승필"
print(ss)
print(ss.split("\n"))
print(ss.splitlines())
# 줄이 바뀌면 줄 바꾸기전 문자열이 하나의 항목인 리스트 생성

ss = "\u2665"
print(ss.join('이혁주 이효재'))
ss = "이혁주 이효재"
print(ss.join('\u2665\u2665'))
# 문자 사이에 특정 문자를 삽입

### 연/월/일 형식으로 문자열 받아 10년 후 날짜를 출력
ss = input("날짜를 입력하세요(연/월/일) : ")

sslist = ss.split('/')
print("입력한 날짜의 10년 후 ==> ", end='')
print(str(int(sslist[0])+10) + '년', end='')
print(sslist[1]+'월', end='')
print(sslist[2]+'일')

# Quiz 연/월/일 2000년대 이전에는 10년 추가, 이후에는 10개월


### 리스트 문자 항목 형식 변경
before = ['2019','12','31']
after = list(map(int, before))
print(after)
# '' 문자열로 취득 받는다
# before라는 대상 리스트 각각의 항목 형식을 바꿔주는 함수 map

### 문자열 정렬 및 채우기
ss = '파이썬'
print(ss.center(10))
# 가운데 정렬, 10이라는 숫자는 자리를 미리 점유
print(ss.center(10, '-'))
# center(자리, 채울문자)
print(ss.ljust(10))
# 왼쪽 정렬
print(ss.rjust(10))
# 오른쪽 정렬
print(ss.zfill(10))
# 오른쪽으로 정렬하고, 나머지 공간 0으로 채움


# Quiz) 다이아몬드 만들기, 높이 입력 받아 정렬,채우기 함수 사용



#### 문자열 구성 파악
# 결과를 True False 형태로 반환
print('11234'.isdigit())
# 문자열 전체가 숫자로 구성 되어 있는지
print('asdf'.isalpha())
# 문자열 전체가 글자(한글/영어)
print('asdf1234'.isalnum())
# 문자열이 숫자와 문자의 조합인지
print('asdf'.islower())
# 문자열이 소문자로 구성되어 있는지
print('ASDF'.isupper())
# 문자열이 대문자로 구성되어 있는지
print('   '.isspace())
# 문자열이 빈공간으로만 구성되어 있는지


#### 대소문자 변환 프로그램
inss, outss = "", ""
ch = ""
count, i = 0, 0

inss = input("문자열을 입력하세요 : ")
count = len(inss)

for i in range(0, count) :
    ch = inss[i]
    if(ord(ch) >= ord("A") and ord(ch) <= ord("Z") ) :
        newch = ch.lower()
    elif (ord(ch) >= ord("a") and ord(ch) <= ord("z")   ) :
        newch =  ch.upper()
    else :
        newch = ch
    outss += newch

print("대소문자 변환 결과 => %s" % outss)

# Quiz) 전화번호를 입력 받으면 010-1235-#### 마지막 네자리가 샵모양으로 출력




############### 문자열 ################
# 문자열은 리스트와 사용하는 방법이 비슷하다
a = '파이썬 개재밋'
aa = ['파','이','썬','','개','재','밋']

print(aa[:5])
print(aa[3:])

print(a[0:5])
print(a[2:])
# 리스트 처럼 첨자를 이용해 출력 가능

# 문자열 더하기 연산
ss = '파이썬' +  '개재밋' + '하하하'
print(ss)
# 문자열 곱하기 연산
ss = "하하하" * 3
print(ss)

print(len(ss))
# 리스트 처럼 len 함수로 길이를 숫자형으로 추출할 수 있다

## 문자열에 문자 사이에 다른 문자 넣기
ss = '안녕하세요 정보보안전문가 양성 과정입니다.'
sslen = len(ss)

for i in range(0,sslen) :
    print(ss[i]+'*', end='')

# Quiz) 문자열을 입력 받고, 띄어쓰기가 있으면 줄을 바꾸기

# 입력 받은 문자열을 거꾸로 출력
inss , outss = '',''
count , i = 0,0

inss = input("문자열을 입력 하세요 : ")
count = len(inss)

for i in range (0, count) :
    outss += inss[count-(i+1)]
print("내용 거꾸로 출력 -> %s" % outss)
print('')

# Quiz) while 문으로 바꿔서 만들어 보자


######## 문자열에서 사용하는 함수 #####
ss = 'Hello hELLo 정보보안 전문가 양성 과정입니다.'
print(ss.upper())
# 영어 소문자를 대문자로 전부 바꿔주는 함수
print(ss.lower())
# 영어 대문자를 전부 소문자로 바꿔주는 함수
print(ss.swapcase())
# 소->대문자, 대->소문자 서로 바꿔주는 함수
print(ss.title())
# 첫문자는 대문자, 나머지는 소문자로 바꿔주는 함수
# 위 4가지 함수는 영어에서만 적용된다.

######## 문자열을 찾는 함수 #######
ss = '파이썬 공부는 너무너무 개재밋,,, 하아 ㅜㅠ 공부 공부 싫어 싫어 집에 갈래'
print(ss.count('공부')), print(ss.find('공부'))
print(ss.rfind('공부')), print(ss.find('리눅스'))
# count : 해당 단어의 개수
# find : (왼쪽) 해당 단어가 있는 위치
# rfind : (오른쪽) 해당 단어가 있는 위치, 위치숫자는 왼쪽부터 센다
# find에서 찾는 단어가 문자열에 없는 경우 -1 값이 출력된다

print(ss.index('공부')), print(ss.rindex('공부'))
print(ss.index('공부',5))
# index는 find랑 동일하게 단어가 있는 위치를 출력
#### find랑 다르게 찾는 단어가 없으면 프로그램 오류 발생
# ('단어', 시작값)


print(ss.startswith('파이썬'),ss.startswith('파이썬',10), ss.endswith('^^'))
# 시작하는 단어가 해당 단어와 일치하면 불대수(True,False)값으로 결과 출력
# endswich : 해당 단어로 끝나면 불대수(True,False)값으로 결과 출력

### 문자열이 괄호로 감싸져 있지 않으면 감싸주는 프로그램
ss = input("문자열 입력 : ")
print("출력 문자열 ===>", end='')

if ss.startswith('(') == False :
    print("(" , end='')
print(ss, end='')

if ss.endswith(')') ==False :
    print(')', end='')
print('')
print("dldikdlkfjdlkfjldj")
# end='' => 여러개의 print()함수에서 출력 된 내용을 한줄에 표시
# print('') 이후에는 줄띄우기

# 문자열의 공백지우는 함수
ww = '   파   이   썬   '
print(ww.strip())
print(ww.rstrip())
print(ww.lstrip())

qq = "---파---이---썬---"
print(qq.strip('-'))
print(qq.rstrip('-'))
print(qq.lstrip('-'))
# 앞뒤로 공백('특수문자') 삭제
# r은 오른쪽 공백, l은 왼쪽 공백 삭제
# 중간문자는 삭제 하지 않는다

#### 중간문자 삭제하는 프로그램
instr = "   한글   Python   프로그래밍   "
outstr = ''

for i in range (0, len(instr)) :
    if instr[i] != ' ' :
        outstr += instr[i]

print("원래 문자열 ==> "+'['+instr+']')
print("공백제거 문자열 ==> "+'['+outstr+']')

# Quiz) "<<<파<<<이>>>썬>>>"  => 파이썬 으로 출력되게 ㄱㄱ

### 문자열 내용 변경
ss = "열심히 파이썬을 공부 중"
print(ss.replace("파이썬","Python"))
print(ss)
# replace : 대체, 해당 단어를 설정한 단어로 교체
# 저장되는 것이 아니라 일시적으로 변경

# 문자열에 문자를 대체하는 프로그램
ss = input("문자열을 영어로 입력하세요 : ")
print("출력할 문자열 ==> " , end='')

for i in range (0, len(ss)) :
    if ss[i] != 'o' :
        print(ss[i], end='')
    else :
        print('$',end='')
print('')

# replace 함수 사용
print("replace 출력 문자열 ==> ", ss.replace('o', '$'))

########## 문자열 분리, 결합 함수  ##########
ss = "Python을 열심히 공부 중"
print(ss.split())
# 띄어 쓰기를 기준으로 리스트의 항목으로 분리 시켜 줌
ss = "최준호, 이영승, 김준혁, 안세종"
print(ss.split(','))
# ~.split("기준") : 기준문자를 기반으로 나눠 리스트로 저장
ss = "최준호\n이영승\n김준혁\n안세종"
print(ss)
print(ss.splitlines())
# 줄이 바뀌면 각가의 항목으로 리스트에 저장
ss = "\u2665"
print(ss.join('이혁주 이효재'))

ss = "이혁주 이효재"
print(ss.join('\u2665\u2665'))
# 문자 사이에 특정 문자를 삽입

# 년/월/일 날짜를 입력 받아 10년 후 날짜 계산

ss = input("날짜를 입력하세요(년/월/일) : ")

sslist = ss.split('/')
print("입력한 날짜의 10년 후 =>", end='')
print(str(int(sslist[0])+10) + '년', end='')
print(sslist[1]+'월' , end='')
print(sslist[2]+'일' , end='')
print('')

# 리스트 문자 항목 형식 변경
# map : 데이터 형식을 변환
before= ['2018','08','21']
after = list(map(int, before))
print(before)
# 리스트의 항목들이 문자열로 취급
print(after)
# 리스트의 항목들을 전부 int 형태로 변환

## 문자열 정렬 및 채우기
ss = "파이썬"
print(ss.center(10))
# 최대길이를 지정하고 문자열을 가운데 정렬
# 10자리를 미리 확보
# 디폴트 값은 null
print(ss.center(10, '-'))
# 비어있는 칸에 특정 문자로 채우기 가능

print(ss.ljust(10,'-'))
# 10자리를 확보 후, 왼쪽으로 정렬
# 비어있는 칸에 특정 문자로 채우기 가능
print(ss.rjust(10))
# 10자리를 확보 후, 오른쪽으로 정렬
print(ss.zfill(10))
# 오른쪽으로 정렬하고, 나머지 공간을 0으로 채움


#### 문자열 구성 파악
# 결과를 True, False 형태로 출력
print('1231654'.isdigit())
# 문자열이 숫자로만 이뤄져있는지 확인
print('asdfqew글자'.isalpha())
# 문자열이 한글/영어(글자)로만 이뤄져있는지 확인
print('asdf1234'.isalnum())
# 문자+숫자 조합으로 이뤄져있는지 확인
print('asdf'.islower())
# 영어 소문자로 이뤄져있는지 확인
print('ASDF'.isupper())
# 영어 대문자로 이뤄져있는지 확인
print('    '.isspace())
# 빈공간으로 구성되어있는지 확인

####### 대소문자 변환 프로그램
inss, outss = '',''
ch = ''
count, i = 0,0

inss = input("문자열을 입력하세요 :")
count = len(inss)

for i in range(0, count) :
    ch = inss[i]
    if(ord(ch) >= ord('A')) and ord(ch) <= ord('Z') :
    # 대문자일 때
        newch = ch.lower()
    elif (ord(ch) >= ord('a')) and ord(ch) <= ord('z'):
    # 소문자일 때
        newch = ch.upper()
    else :
        newch = ch
    outss += newch

print("대소문자 변환 결과 => %s" % outss)

# Quiz) 다아이몬드 그리기 => 다이아몬드의 높이를 홀수로 입력 받기
#       가운데 정렬해서 이쁘게 나오도록

# QUiz) 010-1234-1234 => 입력 받고
#   출력 : 010-1234-****


### 사칙연산 계산기
# 함수 선언
def cal (v1,v2,op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    else :
        print("연산자를 다시 입력해 주세요")
    return result

res = 0
var1 , var2 , oper = 0,0,''

var1 = int(input("첫 번째 숫자 입력: "))
oper = input("연산자 입력(+, -, *, /)")
var2 = int(input("두 번째 숫자 입력: "))

res = cal(var1,var2,oper)
print("계산 결과 : %d %s %d = %d" % (var1,oper,var2,res))

# Quiz) 3번 계산하는 프로그램 만들기
# 쌩코딩 and 함수사용

# Quiz) 숫자 3개 계산하는 프로그램 함수로 만들기


##### 지역변수 전역변수 #######
def func1() :
    a = 10
    # 지역변수 : 함수 내에서만 사용하는 변수
    print("func1() 에서의 a 값 : %d " % a)

def func2() :
    print("func2() 에서의 a 값 : %d " % a)

# 메인코드
a = 50
# 전역변수 : 프로그램 전체(함수 포함)에서 사용하는 변수
func1()
func2()


### 매개 변수 전달 방법
# 1. 매개변수 개수를 정해놓고 사용 (지금까지 우리가 사용한 방식)
# 2. 개수를 정해놓고, 입력이 없으면 기본값을 설정해 사용
# 3. 개수 제한 없음

# 1. 매개변수 개수 정해놓고 사용 (지금까지 우리가 사용한 방식)
def func1(v1,v2) :
    result = 0
    result = v1 + v2
    return result

hap = 0
hap = func1(12,45)
print(hap)

# 2. 개수를 정해놓고, 입력이 없으면 기본값을 설정해 사용
def func1(v1,v2,v3=5) :
    # 매개변수에 입력이 없다면, 기본값을 사용
    result = 0
    result = v1 + v2
    return result

hap = 0
hap = func1(12,45)
print(hap)


# 3. 개수 제한 없음
def func3(*vx) :
    result = 0
    for num in vx :
        result = result + num
    return result

aa = 0
aa = input("숫자입력 ex)34,34,54,24 : ")
aa = list(map(int,aa.split(",")))
print(func3(*aa))

# Quiz) input으로 입력 받아 더하기 갯수 제한 없는 프로그램 작성

############ 로또 번호 추첨  ################
import random
# import : 프로그램 속도를 위해 함수를 따로 빼둔다
# 필요할 때 마다 빼서 쓰는데 그때 쓰는 명령어가 import

def getnumber() :
    return random.randrange(1,46)


lotto = []
num = 0

print("################ 이번주 로또를 추첨 합니다 ################\n")

while True :
    num = getnumber()

    if lotto.count(num) == 0 :
        lotto.append(num)

    if len(lotto) >= 6 :
        break

print("자동 완성 추첨 번호 ==> ", end='')
lotto.sort()
print(lotto, end='')

#for i in range (0,6) :
#    print("%d " % lotto[i], end='')
print()



# Quiz) 6명 이름을 입력받아, 1,2,3등을 추첨을 통해 상금 수여
# 1등 100만원, 2등은 50만원, 3등 20만원
# hint) random.sample(list, 3)





a, b = 0, 0

a = int(input("다이아몬드의 높이의 칸수를 입력하시요(홀수) : "))

for b in range(1, a+1, 1) :
    if b <= a // 2 + 1 :
        print("*" * (2 * b - 1))
    else:
        print("*" * (a - b + 2))

st = '*'
ss = ''
while True :
    k = int(input('\n다이아몬드의 높이의 칸수(홀수)를 입력하세요. <종료시 0> : '))
    if k == 0 :
        break
    for i in range(1, k + 1, 1) :
        if i <= k // 2 + 1 :
            ss = st * (2 * i - 1)
            print(ss.center(k))
        else :
            ss = st * (2 * k - 2 * i + 1)
            print(ss.center(k))
print('프로그램을 종료합니다.')