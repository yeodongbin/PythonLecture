#while 반복 조건
#while (조건):
#   실행문

i = 1 #변수
while i < 11: # 1,2,3,4,5,6,7,8,9,10
    print(i, end = " ")
    i = i + 1 #증감
#Ctrl + c 강제종료
while False :
    print("hi")

while True :
    print("world")
    break

#외부입력 정수 123 => 1+2+3 = 6
#             245 => 2+4+5 = 11
#             1234567 => 1 + 2 + 3 + 4 + 5 + 6 + 7 =>28
# 각 자리에 합을 출력
# while 

num = int(input("Insert Number Value : "))

sum = 0
while num >= 10:
	sum += int(num % 10) 
	num = num // 10   #몫
sum += num
print("각  자리의 합 :", sum)


#반복문 (while, for)
i=1
while i<=10:
    print(i)
    i += 1

a= 1
while True:
    print('hello world',a)
    if a > 10:
        break
    a+=1
else :
    print('good job')
