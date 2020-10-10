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