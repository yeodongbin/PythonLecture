
a = 10            #int
b = 10.1          #float
c = 'hello world' #str
d = -1
e = 'yeo'
f = 'dongbin'
g = 10+2j         #복소수
h = 0b1001        #int
i = 0o1001        #int
j = 0x1001        #int

print(a+b)
print(type(a))
print(dir(a))
print(f[0])
print(f[0:4])
print(f[0:4:2])
print(f[4:0:-1])
print(f[:4:2])
print(f[::2])
print(f[::-1])
print(f[-1])
print(e.upper())
print(e.lower())
print(e.count('y'))

k = '    hello world    '
print(k.strip())
print(k.split(' '))
k_split = k.split(' ')
print('!'.join(k_split))

print('제 이름은 {0}입니다. 제 나이는 {1}입니다.'.format('여동빈',38))
