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
    if (type(x) != list) | (type(y) != list):
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

    #for i in range(2):
    #    for j in range(2):
    # result[i][j] = x[i][0] * y[0][j] + x[i][1] * y[1][j]

    #for i in range(2):
    #   for j in range(2):
    #       for k in range(2):
    # result[i][j] += x[i][k] * y[k][j] 


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
def print_id(**kw_param):
    #global g_num 
    num = 10
    print(type(kw_param))
    print(kw_param)

print_id(id="12345")  #dictionary id = "12345" => key = value

# 지역 전역 변수
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



