#상속 - 이미 정의된 클래스를 상속받아서 사용하는 방법

class Parent():
    def __init__(self):
        self.a = 10
    
    def run(self):
        print("I am running")

class Child(Parent):
    def __init__(self):
        self.b = 20

# 내부 호출 ####################################################
class Car():
    #class variable
    max_speed = 300
    max_people = 5
    def __init__(self):
        print('Car() 생성자 호출')
    def __str__(self):
        print('나는 자동차 입니다.')
    def run(self):
        print("자동차가 달립니다.")
    def stop(self):
        print("자동차가 멈쉽니다.")
        self.stoplight()
    def stoplight(self):
        print('브레이크등이 켜졌습니다.')
        
# 생성자가 자동 생성되어 부모 생성자를 자동호출함
class Hybrid(Car):
    battery_capa = 1000
    battery_km = 300

# 생성자 호출 순서####################################################

class People():
    def __init__(self):
        print("People.__init__()")    

class Athlet(People):
    def __init__(self):
        super().__init__()
        print("Athlet.__init__()")    

class BaseballPlayer(Athlet):
    def __init__(self):
        print("BaseballPlayer.__init__()")    
        super().__init__()

# Override, 다형성 ####################################################
class Animal():
    def sound(self):
        print("동물소리")

class Cat(Animal):
    def sound(self):#Override
        print("야옹")

    def roll(self):
        print('고양이가 구른다.')
    
class Dog(Animal):
    def sound(self):#Override
        print("왈왈")

    def walk(self):
        print("개는 산책중")

class Pig(Animal):
    def sound(self):#Override
        print("꿀꿀")

    def eat(self):
        print("돼지는 먹는중")
    
if __name__ == "__main__":
   animal = Animal()
   cat = Cat()
   dog = Dog()
   pig = Pig()
   animal.sound()
   #animal.walk()
   cat.sound()
   cat.roll()
   dog.sound()
   dog.walk()
   pig.sound()
   pig.eat()

   animals = [cat, dog, pig]
   for obj in animals:
       obj.sound()
       if (isinstance(obj, Dog)):
           obj.walk()

# 다중상속 ####################################################
class Bus():
    def __init__(self):
        print("BUS()")
        #super(Bus, self).__init__()

class Moter():
    def __init__(self):
        print("MOTER()")
        #super(Moter, self).__init__()

class Battery():
    def __init__(self):
        print("BATTERY()")
        #super(Battery, self).__init__()

class ElectroicBus(Bus, Moter,Battery):
    def __init__(self):
        super().__init__()
        # super(ElectroicBus,self).__init__()

        # Bus.__init__(self)
        # Moter.__init__(self)
        # Battery.__init__(self)

# if __name__ == "__main__":
eb = ElectroicBus()











# sample1 ##########################################
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
# 생성자가 자동 생성되어 부모 생성자를 자동호출함
class Hybrid(Car):
    battery = 1000
    batteryKM = 300

k9 = Car()
print(k9.maxPeople)

# sample2 ##########################################
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
