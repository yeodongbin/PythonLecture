def f(x,y):
    z = x+y
    return z
print(f(3,5))

def ff():
    print('1')
    print('2')
    print('3')
    return None
print(4)
ff()
print(ff())

def circle(r):
    width = r * r * 3.14
    return width
print(circle(10))

a= 10
def aplus():
    #global a;
    a+= 10
    return a
print(aplus())


# 함수
# def function_name(argument, ...)
# 재사용, 정의는 실행전
def my_print(argu):
    print(argu)
    print("program end")

def plus(x, y):
    print(x + y)

def min(x, y):
    print(x - y)

def mux(x, y):
    print(x * y)

def div(x, y):
    print(x, y)

def cal(x, op, y):
    result = 0
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    else : 
        print("op입력을 다시해 주세요.")
    return result

def cal_matrix(x, op, y):
    result = [[0,0],[0,0]]
    if (type(x) != list) or (type(y) != list):
        print("x, y 에 2x2 행렬을 넣어 주세요")
        return result

    if op == '+':
        for i in range(2):
            for j in range(2):
                result[i][j] = x[i][j] + y[i][j]
                # print("{0}, {1} : ".format(i,j), end="")
                # print(result[i][j])
    elif op == '-':
        for i in range(2):
            for j in range(2):
                result[i][j] = x[i][j] - y[i][j]
                # print("{0}, {1} : ".format(i,j), end="")
                # print(result[i][j])
    elif op == '*':
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += x[i][k] * y[k][j]
                # print("{0}, {1} : ".format(i,j), end="")
                # print(result[i][j])
    else:
        print("op 입력을 다시 해 주세요")
    return result

    # result[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0]
    # result[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1]
    # result[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0]
    # result[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1]


#Default parameter
def pow(x = 10):
    return x * x
print(pow())


#name parameter
print(pow(x = 20))


#가변길이 파라미터 *
#파라미터가 여러개 입력
def myprint(*num):
    print(num)
#def myprint(num1, num2, num3, num4):
#    print(num1, num2, num3, num4)

myprint(11, 12, 13, 14)
myprint(11, 12, 13)


#키워드 파라미터 **
#dictionary 값을 파라미터로 받는다.
#Keyword Parameter -dictionary parameter
def print_pw1(param):
  print(type(param))
  print(param)

def print_pw2(**kw_param):
  print(type(kw_param))
  print(kw_param)

dic = {"id":12345}
print_pw1(dic)
print_pw2(id ="12345")

print_id(id="12345")  #dictionary id = "12345" => key = value

# 지역 변수, 전역변수
a = 5
def vartest():
    global a
    a = a + 1

vartest()
print(a)

##lambda < 함수 압축
def add(x,y):
    return x+y

result = lambda x,y: x+y
value = result(10,20)

# return (output)
def func_return(param1):#input
    param1 += 1
    return param1       #output

def func_return2():     #input
    num1, num2 = 10, 20
    return num1, num2   #output => tuple(변경불가 list)

return_value = func_return(10)
return_value1, return_value2 = func_return2()

return_value3 = func_return2()

print(return_value, return_value1, return_value2)
print(type(return_value))
print(type(return_value1))
print(type(return_value2))

print(return_value3)
print(type(return_value3))

#<내부함수>
#https://docs.python.org/3/library/functions.html


# 순열, 조합
import itertools

data = [1,2]
for x in itertools.permutations(data,2):
    print(list(x))

data = [1,2,3]
for x in itertools.permutations(data,2):
    print(list(x), end=' ')


#################################################################
# 함수 문제

def sort_mart(**kwargs):
    product = []        # 상품 이름, 가격
    price = []          # 상품 가격

    # 딕셔너리의 key와 value 값을 list로 형변환
    for i in kwargs:
        product.append([i,kwargs[i]])
        price.append(kwargs[i])

    # 리스트 내 element를 알파벳 순으로 정렬
    product.sort()

    # 총액을 구하기 위한 sum 연산 및 마지막 인덱스에 총액 표시 element 추가
    total = sum(price)
    product.append(["total",total])

    # 상품 이름-가격 페어링하여 출력
    for row in product:
        for ele in row:
            print(ele, end="\t")
        print()

sort_mart(tree=1000, egg=500, apple=300, banana=400)


# 소수 문제
def is_prime_number(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True

import math
def is_prime_number2(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

# 소수 문제 M <= x <= N 소수 출력
m, n = map(int, input().split())
array = [ True for i in range(1000001)]
array[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j=2
        while i*j <=n:
            array[i*j] = False
            j+=1

for i in range(m,n+1):
    if array[i]:
        print(i)
