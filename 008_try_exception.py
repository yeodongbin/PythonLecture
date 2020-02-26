
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