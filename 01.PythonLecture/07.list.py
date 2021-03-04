# 리스트, 튜플, 딕셔너리, 셋

l = [10, 20,30, 40]
s = {10,20,30,40, 50}
d = {'one' : 1, 'two':2}
for i in d:
    print(i)

for i in range(10):
    print(i)
    
#리스트 : 변경이 가능한 자료형, 순서가 있는 자료형
l = [100,200,300,400]
print(l)
print(type(l))
len(l)
del(l)

print(l[1])
l[1] = 1000
print(l)
print(dir(l)) # 매서드 확인

l.append(300)
#l.clear()
#l.copy()
l.count(300)
l.extend([100,200,300])
l.index(400)
l.insert(3, 1000) # l[3] 위치에 1000 삽입
l.pop()
l.remove(100)
l.reverse()
l.sort()

#sorted()
#reversed()

#range(Start, stop, step)
print(type(range(10)))
print(list(range(10)))
print(1, list(range(10)))
print(2, list(range(5,10)))
print(3, list(range(2,10,2)))
print(4, list(range(10,5, -1)))
print(5, list(range(-10)))

for i in 'hello world':
    print(i)

for i in range(10):
    print(i)
else:
    print('good job')

#압축형 list, 지능형 list
l = list(range(101))
print(l)

ll = []
print(ll)

for i in range(10):
    ll.append(i)
print(ll)

ll = [i for i in range(10)]
print(ll)

for i in range(2, 10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))

lll = ['{} x {} = {}'.format(i, j, i*j) for i in range(2, 10) for j in range(1,10)]
print(lll)

# 배열 array 
# 리스트 list
a = [10, 20, 30] #a[0] = 10, a[1] = 20, a[2] = 30
print(type(a))

for temp in a:
    print(temp, end=" ")
print()

a[1] = 2000

for i in range(0,3,1):
    print(a[i], end=" ")

# 문제 - 4개 값을 가지는 list < 임의값 4개 입력 전체 합을 출력하시오.
list = [0, 0, 0, 0]
sum = 0
for i in range(0,4):
    list[i] = int(input("Insert value : "))
    sum += list[i]
print("전체 합 : {}".format(sum))

list = []
sum = 0
for i in range(0,4):
    list.append(int(input("Insert value : ")))
    sum += list[i]
print("전체 합 : {}".format(sum))

#초기화(Dynamic array)
a = []       #list명은 정했지만 저장 갯수 X
a = [0,0,0]  #list명은 정하고 저장 갯수 3
a = [0, "yeo", True]

#슬라이싱(Slicing)
print(a[0])    # 0
print(a[0:2])  # 0 yeo
print(a[-1])   # True
print(a[:])    # 0 yeo True

#추가 append(185), insert expend
a.append(185)
print(a)
a.insert(0,"first")  # 0 index "first" 값
print(a)
a.insert(1,"second")  # 1 index "second" 값
print(a)

#변경 list[index] = 값
a[3] = 184
print(a)

#삭제 del list[index], remove, pop
del a[0]
print(a[:])

#병합 +
b = ["dongbin", False, 100]
c = a + b
print(c,len(c),end="\n") 
# ['yeo', True, 184, "dongbin", False, 100]

d = a
print(d)
d.append(b)
print(d,len(d),end="\n") 
# ['yeo', True, 184, ["dongbin", False, 100]]

#반복
d = a * 2
print(d)

#검색
string = "my name is yeo dongbin".split()
index = string.index("yeo") #11
count = string.count("m")   #2
print(index, count)

# 얇은 복사, 깊은 복사 
alist = [1,2,3,4]
blist = alist #얇은 복사
print(id(alist))
print(id(blist))
print(blist)
alist[3] = 10
print(blist)

#Stack / append() pop()
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)
print(stack.pop())
print(stack)

#Queue / append() pop(0)
queue = []
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)
print(queue.pop(0))
print(queue)

# list comprehension : 코드를 짧게 쓰자
list = []
for i in range(6):
    if (i%2 == 1):
        list.append(i)
print(list)

list2 = [i for i in range(6) if i%2 == 1]
print(list2)

# x 1 ~ 5 , y 1 ~ 5 =>  x * y => 25가지
# 1*1 1*2 1*3 .... 
list3 = [x*y for x in range(1,6,1) for y in range(1,6,1)]
print(list3)

rl = list(range(100,500,100))
print(rl)

rl2 = [i for i in range(100,500,100)]
print(rl2)

rl3 = ['{}*{}={}'.format(i,j,j*j) for i in range(2,10) for j in range(1,10)]
print(rl3)

rl4 = [ 10 if True else 20]
rl5 = [ i for i in range(10) if (i % 2 ==0) ]
print(rl5)


### list list = 1D => 2D
list2D = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(list2D)

for i in range(3):
    for j in range(3):
        print(list2D[i][j], end=" ")
    print()

# 다양한 리스트 저장 방법
l = [(1,10),(2,20),(3,30),(4,40)]
print(l[2][1])
for i in l:
    print(i)

for i, j in l:
    print(i, j)

for i, j in enumerate(range(100,1000,100),1):
    print(i,j)

for i in range(10):
    pass
    print('hello world')

for i in range(10):
    continue
    print('hello world')
    
    
##############################################################
#문제 - 피보나츠 수열
1 2 3 5 8 13 21 34 55... 100개 그리고 합
pibo_list = []
pibo_list.append(1)
pibo_list.append(2)

for i in range(0,8,1): #98 count
    pibo_list.append(pibo_list[i]+pibo_list[i+1])
    print(pibo_list)

sum = 0 
for element in pibo_list:# 1 2 3 5 8 13 21 34 55 89
    print(element)
    sum += element

print("Total : %d" %sum)


#문제- 10개 짜리 피보나츠 수열을 list로 구현, 반전 시키지오
pibo = []
pibo.append(0)
pibo.append(1)
print(pibo)
for i in range(2,10,1):
    temp = pibo[i-2] + pibo[i-1]
    pibo.append(temp)

print(pibo)

for i in range(0,5,1) :
    pibo[i], pibo[len(pibo)-1-i] = pibo[len(pibo)-1-i], pibo[i]

pibo2 = []

for i in range(0,10,1) :
    temp = pibo[9-i]
    pibo2.append(temp)

print(pibo2)

#문제 lotto 6자리가 안 겹치도록 만드시오.(10/18 과제)
#해답1
from random import *

lotto=[]
while(len(lotto)<6):
    rand_num = randint(1,45)  # 1~45 까지 랜덤값을 만들어줌
    if (rand_num not in lotto):
        lotto.append(rand_num)
lotto.sort()                  #순차 정렬
print(lotto)

#해답2
from random import *

lotto = [0, 0, 0, 0, 0, 0]          # list 초기화, 6자리 설정.
for i in range(0, 6, 1):            # 6회 반복
    lotto[i] = randint(1,45)        # 1 ~ 45 사이 랜덤값 추출하여 lotto[i]에 설정
    count = lotto.count(lotto[i])   # 추출된 lotto[i]값이 lotto 리스트에 있는지 검색.
    if count == 0:                  # count값이 0인 경우, 중복값 없으므로 리스트에 추가.
        lotto.append(lotto[i])
     
lotto.sort(reverse=True)
#lotto.reverse()                    # index 기분 역전
print(lotto)

##############################################################

#list list = 1D => 2D

#  1  2  3  4  5
# 10  9  8  7  6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
#1
matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(0) #[0,0,0,0,0]
    matrix.append(row)
print(matrix)

#2
matrix = [[0 for i in range(5)] for j in range(5)]
print(matrix)

#3 얇은 복사 발생 문제
# matrix = [[0]*5]*5
# print(matrix)

num = 1
for i in range(5):
    if i%2 == 0:
        for j in range(5):
            matrix[i][j] = num 
            num += 1
    else :
        for j in range(4,-1,-1):
            matrix[i][j] = num 
            num += 1

# 출력부
for i in range(5):
    for j in range(5):
        print("{0:>2}".format(matrix[i][j]), end=" ")
    print()
print()

for arr in matrix:
    for num in arr:
        print("{0:>2}".format(num), end=" ")
    print()

print(matrix)


#문제 - 2D list(matrix) 90' rotate
def rotate_a_matrix_by_90_degred(a):
    row_length = len(a)
    column_length = len(a[0])
    res =[[0]*row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]

    return res

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(rotate_a_matrix_by_90_degred(a))


    
