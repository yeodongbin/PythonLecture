#변수명, = 대입연산자, 값
a = 10    #int
b = -10   
c = 10.1  #float point
d = -10.2
e = "hello world" #string
f = 'abcdefghij'
g = 10 + 2j #복소수
h = 0b010   #2진수   2 int
i = 0o010   #8진수   8 int 
j = 0x00A   #16진수 10 int

#print(a + b)
#print(type(a)) # 변수 타입 확인
#print(dir(a))  # 내부 메서드 확인
print(f[0])    # abcdefghij 문자열 = 문자의 연속
print(f[1])
print(f[0:4])   # 0 1 2 3 / 4
print(f[0:4:2]) # 0(a) 1 2(c) 3 / 4
print(f[4:0:-1]) # 0(a) 1(b) 2(c) 3(d) 4(e) 
print(f[4:0:-2])
print(f[:10])
print(f[:])
print(f[::2])
print(f[::-1])
print(f[-1])
print(f[-2])

#print(dir(f))
f_upper = f.upper()
print(f_upper)
print(f_upper.lower())

f_upper = f_upper + f_upper
print(f_upper)
print(f_upper.count('AB'))

k = "    yeo dongbin    "
print(k)
print(k.strip())
print(k.strip().split(' '))

j = "Life is too short"
print(j.replace("Life", "Your leg"))

l = "winter\tis\ncoming"
print(l)

print(e.lower())
print(e.count('y'))

k = '    hello world    '
print(k.strip())
print(k.split(' '))
k_split = k.split(' ')
print('!'.join(k_split))

print('제 이름은 {0}입니다. 제 나이는 {1}입니다.'.format('여동빈',38))


# 변수 : 값을 담아 내는 그릇, 스티커
# 종류 : 정수, 실수, 문자열, bool (참, 거짓)
# 주의 : 
# 1. 변수이름 대소문자 구분
# 2. 문자(영), 숫자, _
# 3. 변수명 숫자로 안됨 ex) 0name (x)
# 4. 예약어(if , while, else, elif) X

# bool -> 조건식에 사용됨 (condition)
result = True
print(result)
result = False
print(result)

year = '2020' #int => str
month = '10'
day = '11'
print(year , month , day)
#2020/10/11 (양력)

print(year , month , day, sep = '/')
print(year , month , day, sep = '/' , end = '(양력)\n')

# 문자열끼리 + => 문자열 붙이기 'yeo' + 'dongbin' = yeodongbin
# 숫자끼리 + => 더하기 
d = year  + '/' +  month  + '/'+ day + '(양력)'
print(d)

# 타입변환 ex) int => str
# float()와 int() 함수를 사용하여 데이터의 형 변환 가능
e = 10 # int 10
print(type(e))
# 1010
print(e*101)

# str(10) => str '10'
f = str(e) + str(e)
print(f) # '10' + '10' => 1010
print(type(f)) # f : str
# print(f + 100)
print(int(f) + 100)

print(bool(' '))  # True
print(bool(''))   # False
print(bool(0))    # False
print(bool(1))    # True
print(bool(-1))   # True
print(bool())     # False
print(bool(None)) # False

a = 10 # <= 컴퓨터 연산 방향
#10 = a

a = b = c = d = 10
print(a, b, c, d)

#진수 표현
print(0b0010) # 0010(2) = 2
print(0o0010) # 0010(8) = 8
print(0x0010) # 0010(16) = 16
print(bin(2))  # 2   => 0b10(2) 
print(oct(8))  # 8  => 0o10(8)
print(hex(16)) # 16 => 0x10(16)
print(int('0010',2))  # 0010(2) = 2
print(int('0010',8))  # 0010(8) = 8
print(int('0010',16)) # 0010(16) = 16

