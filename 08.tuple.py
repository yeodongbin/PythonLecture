#----------------------------------------
#튜플 : 순서가 있고 변경이 불가능한 자료형

# list = []
# tuple = ()
# 읽기전용 -> 추가, 수정 삭제 X
t = (10, 20, 30)
print(type(t))
print(t)
print(dir(t))

t = (100, 200, 300)
print(t)
del t[0]
t[0] = 400
print(type(t))
print(dir(t))

print(t.count(10)) # 10과 동일한 항목 갯수 확인
print(t.index(10)) # 10을 찾아 index 반환   

#상수 용도 
t1 = 1,2
t2 = 1,2,3
print(type(t1))
print(type(t2))
print(t2)

t3 = 4          # tuple or value 저장? value
t6 = (6)
print(type(t3))
print(type(t6))

t4 = 5,
t5 = (5,)
print(type(t4))
print(type(t5))

#t5.append(7)  #튜플 추가 안됨
#t1[2] = 40    #튜플 수정 안됨
#del t1[2]     #튜플 삭제 안됨

print(t1 + t2)  # 사용법은 동일
print(t1 * 3)   # 사용법은 동일
print(t1[0] + t1[1])

listA = [1,2,3,4,5]
tupleA = tuple(listA)
print(type(tupleA))
print(tupleA)

for i in tupleA:
    print(i)

listB = list(tupleA)
print(type(listB))
print(listB)





