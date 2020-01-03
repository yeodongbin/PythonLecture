# Class
# 1. class name 첫 문자가 대문자
# 2. class는 대부분 직접 만지지 않습니다.
# 3. 붕어빵 찍는 틀로 생각합니다. instance 는 붕어빵이다.

class Car():
    maxSpeed = 300
    maxPeople = 5
    def start(self):
        print('Start')
    def stop(self):
        print('Stop')
    def __str__(self):
        return 'hello world'
    def __init__(self):
        print('Instance가 만들어 졌습니다.')

class Hybrid(Car):
    battery = 1000
    batteryKM = 300

k9 = Car()
print(k9.maxPeople)

#https://docs.python.org/3/library/functions.html