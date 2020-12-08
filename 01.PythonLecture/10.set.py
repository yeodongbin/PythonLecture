
#----------------------------------------
#셋 : 숫서가 없고 값의 중복을 허락하지 않는 자료형
s = {100,200,300,400,500}
ss = {1,2,3}

print(s)
print(type(s))
print(dir(s))
print(set('aaabbbcccff'))
print(s.union(ss))
print(s.intersection(ss))
print(s.difference(ss))
print(s.update(ss))

print(ss.add(4))
print(ss.remove(4))
print(ss.discard(4))
print(ss.pop())

sa = set('ABCDEFG')
sb = set('DEFGHIJ')
print(sa-sb)
print(sa|sb)
print(sa&sb)
print(sa^sb)

# 집합 set 1. 겹치지 않고  2. 순서가 없음
# dic0 = {} #dictionary
# dic = {"key":"values"}
# s = set() #set 초기화

set1 = {100, 200, 300, '100', 300}
print(type(set1))
print(set1)
print(dir(set1))

set2 = set()
print(type(set2))

set3 = {"apple"}
set3 = set("apple")
print(set3)

set4 = set("ant")
print(set4)

print(set3 - set4) #차집합
print(set3 | set4) #합집합
print(set3 & set4) #교집합

#추가 add update
set5 = set()
set5.add(100)
set5.add(200)
set5.add(300)
print(set5)
set5.add(200)
print(set5)

set5.update([400, 500, 100])
print(set5)

#삭제 discard remove
set5.discard(100)
print(set5) 

# set5.remove(100)
# print(set5)

#집합 연산자 difference intersection union
set6 = {'a','b','c','d','e'}
set7 = {'a','b','c','f','g'}

set8 = set6.difference(set7)    #de
print(set8)
set8 = set6.intersection(set7)  #abc
print(set8)
set8 = set6.union(set7)         #abcdefg
print(set8)

#형 변환
l_s = set([1,2,3])
s_t = tuple({5,6,7})
st_l = list('hello')
l_d = dic([1,2],[3,4])
l_d2 = dic([(5,6),(7,8)])