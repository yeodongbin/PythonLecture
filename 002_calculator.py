a = 2020
b = 1
c = 3
print(a,b,c, sep='/', end = ' ')
print(a,b,c)

d = 10
e = '10'
print (10 + int(e))
print (str(d) + e)

f = True
g = False
print(type(a))

print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool())
print(bool(None))

h = 3
j = 10
print(h + j)
print(h - j )
print(j / h ) #float
print(j // h ) #int
print(h * j )
print(h ** j )
print(h % j )

#비교 연산
print(h >= j)
print(h > j )
print(j < h )
print(j <= h )
print(h == j )
print(h !=  j )

#논리 연산
print(f and g)
print(f or g)
print(not f)

#할당 연산
k =10
k = k +10
k += 10
print(k)

#bit 연산
a = 40
b = 14
print( a & b)
# & / ~
print(bin(a)[2:].zfill(6))
print(bin(b)[2:].zfill(6))
# 101000
# 001110
# ------ And 연산
# 001000


