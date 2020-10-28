## sample
class Car():
    __max_speed = 300

    def __init__(self):
        self.__max_gas = 40
        self.__current_gas = 0
        self.__speed = 0
        self.__gas_step = 2

    def check_gas(self):       #getter gas
        print(f"Current Gas : {self.__current_gas} L")
        
    def insert_gas(self, gas): #setter gas
        free_space_gas = self.__max_gas -self.__current_gas
        if (free_space_gas >= gas):
            self.__current_gas = self.__current_gas + gas
        else :
            print(f"!! 주유용량이 초과하였습니다. {free_space_gas} L 이하로 주류해 주세요!!")
    
    def run(self):
        if (self.__current_gas >= 0) and (self.__speed < Car.__max_speed) :
            if self.__current_gas < self.__gas_step :
                print("연료가 부족합니다.")
                return 
            else : #연료가 부족하지 않은 상태
                if self.__speed <  Car.__max_speed:
                    self.__speed += 30  # if 310
                    self.__speed %= Car.__max_speed
                    self.__current_gas = self.__current_gas - self.__gas_step
                    print(f"차가 달립니다. : {self.__speed} km") 
                elif self.__speed >= Car.__max_speed:
                    print("최고속도에 도달하였습니다.") 
            
    def stop(self):
        if self.__speed >= 50 :
            self.__speed = self.__speed - 50
            print(f"{self.__speed} km 입니다.")
        else :
            self.__speed = 0
            print("정차했습니다.")

class Hybrid(Car):
    pass

if __name__ == "__main__":
    niro = Hybrid()
    niro.check_gas()
    niro.run()
    niro.insert_gas(40)
    niro.check_gas()
    niro.run()
    niro.run()
    niro.run()
    niro.stop()
    niro.check_gas()






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

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()