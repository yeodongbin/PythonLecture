# Class
# 1. class name 첫 문자가 대문자
# 2. class는 대부분 직접 만지지 않습니다.
# 3. 붕어빵 찍는 틀로 생각합니다. instance 는 붕어빵이다.

# sample1 ##########################################
class Dog:
    """A simple attempt to model a dog."""  
  
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def run(self):
        print(f"{self.name}가 달리다")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# sample2 ##########################################

class Car:
    #속성
    maker = ''
    model = ''
    year = 0
    speed = 0

    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def set_maker(self ,maker):
        self.maker = maker

    def get_maker(self):
        return self.maker

    def print_info(self):
        print("{}, {}, {}".format(self.maker, self.model, self.year))


# problem1 ##########################################
# Restaurant
# 생성자 : 식당이름,식당종류,식당개업연도
# 식당소개() describe_restaurant() :
# 식당메뉴소개() 매서드명 자유:
# 식당열기() 매서드명 자유 : 식당이 열렸습니다.
# 식당닫기() 매서드명 자유 : 식당이 닫혔습니다.
# 식당 1,2,3 개업
class Restaurant():
    foot_type = "프랑스요리" #class variable 전역변수 or 상수 개념으로 이해

    def __init__(self, name, foot_type, year):
        self.name = name          #instance variable 
        self.foot_type = foot_type
        self.year = year

    def describe(self):
        print("{}년에 개업한 {}입니다.".format(self.year, self.name))

    def menu(self):
        print("{}식당의 메뉴는 {}입니다.".format(self.name, self.foot_type))

    def open(self):
        print("식당이 열렸습니다.")

    def close(self):
        print("식당이 닫혔습니다.")

R1 = Restaurant("백반", "한정식", "2020")
R2 = Restaurant("중화반점", "중식", "2019")
R3 = Restaurant("돈라멘", "일식", "2018")

R1.describe()
R2.describe()
R3.describe()

R1.menu()
R2.menu()
R3.menu()

print(Restaurant.foot_type)
print(R1.foot_type)

# sample 2 ### computer ################################
class Computer:
        maker = ''
        price = ''
        power = False
        def __init__(self,maker, price):
            self.maker=maker
            self.price=price
        def play_game(self):
            if self.power == True:
                print("Play Game Start")
            else :
                print("Power가 {} 입니다.".format(self.power))
        def power_on(self):
            self.power = True
        def power_off(self):
            self.power = False
        def pc_info(self):
            print(self.maker, self.price)

my_pc = Computer('samsung',2000000)
my_pc.power_on()
my_pc.play_game()
my_pc.pc_info()


# sample 3 ### starcraft ################################
# SCV : worker
# hp
# mp
# attack(scv)
# move(x, y)
# mine(mineral)
# fix(scv)

class SCV:
    def __init__(self, num):
        self.__hp = 50  # 캡슐화 (외부 보이지 않는다.)
        self.__mp = 0
        self.scv_num = num
        self.x = 0
        self.y = 0

    #getter
    def get_mp(self):
        print("{}".format(self.__mp))
        return self.__mp

    #setter
    def set_mp(self, mp):
        self.__mp = mp
        print("{}".format(self.__mp))

    def move(self, x, y):
        self.x = x
        self.y = y

    def attack(self, scv):
        scv.__hp = scv.__hp - 10

    def fix(self, scv):
        scv.__hp = scv.__hp + 10

    def check(self):
        print(f"SCV({self.scv_num}) : ({self.__hp}, {self.__mp})")


scv1 = SCV(1)
scv1.check()

scv2 = SCV(2)
scv2.check()

scv1.attack(scv2)
scv1.check()
scv2.check()

scv1.fix(scv2)
scv1.check()
scv2.check()

#문제 - User 클래스
# - 캡슐화
# first_name
# last_name
# age
# height
# weight

# set_user(first_name, last_name)
# set_private(age, height, weight)
# describe(user)
# greet_user()
# => 안녕하세요. {이름} 입니다.

class User:
    def __init__(self):
        pass

    def set_user(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def set_private(self, age, height, weight):
        self.__age = age
        self.__height = height
        self.__weight = weight

    def describe(self):
        print("first_name : {}\nlast_name : {}\nage : {}\nheight : {}\nweight : {}\n"
                .format(self.__first_name, self.__last_name, self.__age, 
                        self.__height, self.__weight))

    def greet_user(self):
        print("안녕하세요. {}{}입니다.".format(self.__first_name, self.__last_name))


user = User()
user.set_user("유", "소윤")
user.set_private(24, 180, 50)
user.describe()
user.greet_user()


#Super Car
#속성
#name, power
#Speed 
#max_speed =200
#gas =200

#기능
#run() 시 +30km -10 gas
#stop() 멈춤 -40
#power() 시동, speed >0 때 시동이 꺼지면 안됨
#booster() 5초간 300km -> 200 km로 바뀜 -50gas
import time

class SuperCar :
    def __init__(self,name) :
        self.name=name
        self.power = False
        self.speed = 0
        self.max_speed = 200
        self.gas = 200

    def powerOn(self):
        self.power = True
    
    def powerOFF(self):
        if self.speed == 0:
            self.power = False
        else : 
            print("시동을 끌수 없습니다.")

    def stop(self):  
        if self.speed >= 40:    
            self.speed -= 40
        else :
            self.speed = 0
        
    def check_speed(self):
        print("현재 속도 : {}".format(self.speed))

    def check_gas(self):
        print("현재 연료량 : {}".format(self.gas))

    def print_info(self):
        self.check_speed()
        self.check_gas()

    def run(self):
        if self.power == False :
            print('시동을 걸어주세요')
        elif self.power == True :
            if self.gas>= 10 :
                if self.speed <= self.max_speed - 30 : # 0 ~ 170
                    self.speed += 30
                    self.gas -= 10
                elif self.max_speed - 30 < self.speed < self.max_speed: # 170 < speed < 200~ 
                    self.speed = self.max_speed
                    self.gas -= 10
                elif self.speed >= self.max_speed:     # 200 <= speed
                    print(f'최고속도로 달리고 있습니다.')
                
            else :
                print(f'연료가 부족합니다.')
            self.print_info()

    def booster(self):
        if self.power == False :
            print('시동을 걸어주세요')
        elif self.power == True :
            if self.gas > 50 :
                self.speed = 300
                self.gas -=50
                self.print_info()
                print("Booster On!!")
                for i in range(5):    
                    time.sleep(1)
                    print("{}초".format(5-i))
                print("Booster Off!!")
                self.speed = self.max_speed
            else :
                print(f'연료가 부족합니다.')
        self.print_info()
        
supercar = SuperCar('Asurada')
supercar.powerOn()
supercar.run()
supercar.booster()

supercar.powerOFF()
supercar.run()

