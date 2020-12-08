
# 예외 처리
# try:
# except:

# try:
# except ZeroDivisionError:

# try:
# except ZeroDivisionError as e:

# try:
# except ZeroDivisionError as e:
# except IndexError as e:

# try:
# except (ZeroDivisionError, IndexError) as e:

# try:
# except ZeroDivisionError:
#   pass

# try:
# finally:


class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird): #Bird 상속
    def fly(self):
        print("very fast")

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별병입니다."

def say_nick(nick):
    if nick == 'foo':
        raise MyError()

    print(nick)

say_nick("foo")

    
# eagle = Eagle()
# eagle.fly()

################################################

#a / b => 'b!= 0'
a = 10
b = 0
if ( b != 0):
    print(a / b)

#Excetpion class 
try:
    #print(10 / 0)
    str = 'abcdef'
    print(str[7])
except ZeroDivisionError :
    print("ZeroDivisionError 발생")
except IndexError : 
    print("IndexError 발생")
else : #Error 발생하지 않으면 동작
    print("Error 발생하지 않으면 동작")
finally:
    print("무조건 동작")

def get_pizza_name():
    print("banolrim pizza")
    if True :
        raise NotImplementedError

get_pizza_name()