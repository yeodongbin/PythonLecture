# 반복문
# for   : 반복 횟수
# for (변수) in range(시작값, 종료값, 증가값):
#   실행문
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

for (i) in range(0, 100, 1): # 0 1 2 3 4 5 6 7 8 ... 99
    #print(i)
    pass

for (j) in range(5, -1 ,-1):   # 5 4 3 2 1 0
    print(j, end=' ')
print()

# 1~10 합
sum = 0
for k in range(1,11,1):  # k = 1, 2, 3, 4 ... 10
    print(k, end = " ") 
    sum = sum + k        # sum = 1, 3, 6 ....
print("\nsum = %d" %sum)


# 123부터 ~ 500까지 짝수 모두 더하기
sum = 0
for value in range(123, 501, 1):
    if value % 2 == 0:
        sum += value 
        #print(value, end=" ")
print("sum={}".format(sum))

sum = 0 #변수 초기화
for value in range(124, 501, 2):
        sum += value 
        #print(value, end=" ")
print("sum={}".format(sum))


# 구구단 (2단)
# 2 * 1 = 2
# 2 * 2 = 4 
# ...
# 2 * 9 = 18
dan, i = 2, 1
for i in range(1,10,1):
    print("{0} * {1} = {2}".format(dan,i,dan*i))
print()

# 2 ~ 9단
for dan in range(2,10,1):
    for i in range(1,10,1):
        print("{0} * {1} = {2}"
        .format(dan,i,dan*i))

#=> 2 ~ 9단 * 1 ~ 9
for i in range(1, 10, 1):
    for dan in range(2, 10, 1):      
        print("{0} * {1} = {2}"
        .format(dan, i, dan*i), end='\t')
    print()
print()
for i in range(1, 10, 1):
    for dan in range(2, 10, 1):
        if (i==(dan-1)):
            print("         ", end="\t")
        else :
            print("{0} * {1} = {2}".format(dan, i, dan*i), end="\t")
    print()      


############################### <문 제> ###################################

# 문제 - 약수 : 나누어 떨어지는 수 15 => 1 , 3, 5 , 15
# 15 => 1 ~ 15
# num = int(input("값 입력 : "))
# print("{}의 약수 : ".format(num), end="")
# for k in range (1,num+1,1):#1~15
#     if (num % k == 0) :#약수
#         print(k, end=", ")


# 문제 - 1 ~ 100 소수만 출력하시오. 소수 : 7 => 1, 7 나누어 떨어져야 함
# 소수
# count_sosu = 0
# for i in range(2,101,1):
#     count = 0
#     for j in range(1,i+1,1): # 5 : j = 1,2,3,4,5
#         if (i % j == 0):
#             count += 1

#     if(count == 2):
#         print(i, end = ", ")
#         count_sosu += 1

# print("\n소수의 갯수 : %d" %count_sosu)

# 문제 : 4x + 5y = 60, 경우의 수, 1<= x,y <=100
for x in range(1,101,1): #100
    for y in range(1,101,1): #100
        if((4 * x) + (5 * y)) == 60: #10000
            print ("( %d, %d )" %(x,y))

#문제 별찍기
# * 
# **
# ***
# ****
# *****

# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print("*", end="")
#     print()

# for i in range(1,6,1):
#     print("*" * i)


# 문제
#     * 
#    **
#   ***
#  ****
# *****

# for i in range(5,0,-1):
#     for j in range(1,6,1):
#         if(i>j):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# for i in range(4,-1,-1):
#     print(" " * i, end="")
#     print("*" * (5 -i))



# 문제 - 임의 값 2개를 입력받아 최대공약수, 최소공배수를 찾으시오
num1=int(input("임의값1 : "))
num2=int(input("임의값2 : "))

max = num1 if (num1 > num2) else num2
min = num1 if (num1 < num2) else num2

#최소공배수
for x in range(max, (num1*num2)+1, 1):
    if (x%num1 ==0)&(x%num2 ==0):
        l = x 
        break

#최대공약수
for y in range(1, min+1, 1):
    if (num1 % y == 0)&(num2 % y ==0):
        g = y

print("최소공배수 =", l)
print("최대공약수 =", g)






    














