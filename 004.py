# 리스트, 튜플, 딕셔너리, 셋

#-------------------------------------------
#리스트 : 변경이 가능한 자료형, 순서가 있는 자료형
l = [100,200,300,400]
print(l)
print(type(l))

print(l[1])
l[1] = 1000
print(l)
print(dir(l))

l.append(300)
#l.clear()
#l.copy()
l.count(300)
l.extend([100,200,300])
l.index(400)
l.insert(3, 1000)
l.pop()
l.remove(100)
l.reverse()
l.sort()
#sorted()
#reversed()

#----------------------------------------
#튜플 : 순서가 있고 변경이 불가능한 자료형

t = (100, 200, 300)
print(t)
print(type(t))
print(dir(t))


#----------------------------------------
#셋 : 숫서가 없고 값의 중복을 허락하지 않는 자료형
s = {100,200,300,400,500}
ss = {1,2,3}

print(s)
print(type(s))
print(dir(s))
print(set('aaabbbcccff'))
print(s.union(ss))

#----------------------------------------
#딕셔너리 : 키와 벨류, 키의 중복을 허락 하지 않는
d = {'one' : 10, 'two' : 20}
print(d['one'])
print(type(d))
print(dir(d))
print(d.values())
print(d.keys())
print(d.items())

l = list(d.items())
print(l[0][1])

jeju = {'banana' : 5000, 'orange': 2000}
seoul = jeju.copy()





