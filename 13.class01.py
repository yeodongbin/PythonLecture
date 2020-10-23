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



# problem1 ##########################################
# 01. Restaurant 클래스를 만드세요
# __init__() => Restaurant_name, cuisine_type
# describe_restaurant()
# open_restaurant()
# 02. 3개의 Restaurant을 만드시오

# 03 사용자: User 클래스
# setting_user(...)
# first_name
# last_name
# age
# height
# weight
# describe_user()
# greet_user()


