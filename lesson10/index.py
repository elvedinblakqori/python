from abc import ABC, abstractmethod

from rich.box import SQUARE


# class Student:
   # def __init__(self, name, age):
     #   self.__name__ = name
    #    self.__age = age

   # def get_name(self):
    #    return self.__name

   # def set_name(self, name):
     #   self.__name = name

    #def get_age(self):
   #     return self.__age

 #   def set_age(self, age):
  #      self.__age = age


#student1 = Student("Elvedin", 17)
#print("Name: ", student1.get_name())
#student1.set_name("unknown")
#print("Updated name: ",student1.get_name())

#print("Age", student1.get_age())
#student1.set_age(18)
#print("Updated age: ", student1.get_age())



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Cicrle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

circle = Circle(7)
square = Square(10)

print(circle.area())
print(square.area())
