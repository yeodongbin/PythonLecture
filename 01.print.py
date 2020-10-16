# first file (comment) 주석
"""
파이썬 공부중
"""

#print(문자 숫자 변수 등등...)
#"hello world" 'hello world'
print("hello world")
print('hello world')
print(10)
print(20)

a = 10   # 10 정수값 integer decimal
b = 10.1 # 실수값 float 
c = "yeodongbin" # yeodongbin 문자열 string

print(a, b, c)

# 가변정수 %d
height = 184
print("내 키는 %d cm 입니다." %height)
print("내 키는 174cm 입니다.")

# 실수 %f
foot_size = 28.5
print("내 발사이즈는 %0.1f cm 입니다." %foot_size )

# 문자열 %s
name = "yeodongbin"
print("My name is %s" %name)

# 변수명 => 명사 스네이크법 foot_size 
#               낙타법     footSize
# 함수명 => 동사 

percent = 50
print("세일 %d%%" %percent)
print("키 = %d, 발사이즈 = %.1f" %(height, foot_size))
print('%f' %3.14)

my_name = "My name is %s" %'yeodongbin'
print(my_name)

#파이썬 스타일 출력 => 결과는 똑같다
my_first_name = "My first name is {}".format('yeo')
print(my_first_name)

my_first_name = "yeo"
my_middle_name = "dongbin"
my_name = "{} {}".format(my_first_name,my_middle_name)
print(my_name)

print("{} x {} = {}".format(2,3,6))
print("{1} x {0} = {2}".format(2,3,6))


