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

l = [10, 20,30, 40]
s = {10,20,30,40, 50}
d = {'one' : 1, 'two':2}
for i in d:
    print(i)

for i in range(10):
    print(i)

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











