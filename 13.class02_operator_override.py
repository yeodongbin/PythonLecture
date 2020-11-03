# Operator Overloading
# +, -, *, @, /, //, %, divmod()
# + object.__add__(self, other)   
# - object.__sub__(self, other)
# * object.__mul__(self, other)
# @ object.__matmul__(self, other)
# / object.__truediv__(self, other)
# // object.__floordiv__(self, other)
# % object.__mod__(self, other)
# (몫, 나머지) object.__divmod__(self, other)
# pow object.__pow__(self, other[, modulo])
# < object.__lshift__(self, other)
# > object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)


class Complex:
    def __init__(self, i, j): 
        self.__i = i
        self.__j = j

    def __add__(self, other):
        i = self.__i + other.__i
        j = self.__j + other.__j
        return Complex(i, j)

    def __sub__(self, other):
        i = self.__i - other.__i
        j = self.__j - other.__j
        return Complex(i, j)

    def __mul__(self, other):
        i = (self.__i * other.__i)-(self.__j * other.__j)
        j = (self.__i * other.__j)+(self.__i * other.__j)
        return Complex(i, j)

    # 숙제 : 복소수의 나눗셈
    def __truediv__(self, other):
        i = 0
        j = 0
        return Complex(i, j)

    def __str__(self):# print() 호출
        return str(self.__i) + " + " + str(self.__j) + "i"

cp1 = Complex(1,2)
cp2 = Complex(5,6)
cp3 = cp1 + cp2
print(cp3)
cp4 = cp1 * cp2
print(cp4)


# class -> instance 
# 생성자 __init__
# 소멸자 __del__  <- GC가 호출한다.


class Node:
    def __init__(self):
        print("생성자 호출")

    def __del__(self):
        print("소멸자 호출")

print("시작")
node = Node()

print("프로그램 종료")





