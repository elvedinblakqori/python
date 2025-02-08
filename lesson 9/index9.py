class Animal:
    def sound(self):
        print("Make some animal noises")

class Dog():
    def sound(self):
        print(" Woof Woof !!")

class Cat():
    def sound(self):
        print(" Meow Meow !!")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

class Vehicle:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year{self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, bodystyle):
        super().__init__(make, model, year)
        self.body_style = bodystyle

class ElectricCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("charging the battery of electric car !")

tesla = ElectricCar("Tesla", "Cybertruck", 2024, "Square", "350km")
tesla.display_info()
print("Body style:", tesla.body_style)
print("battery capacity:", tesla.battery_capacity)
tesla.charge()


