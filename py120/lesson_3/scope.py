class Dog:
    def __init__(self, breed):
        self._breed = breed
    
    def get_breed(self):
        return self._breed

samson = Dog('Golden Retreiver')
fido = Dog('Poopdle')

print(samson.get_breed())
print(fido.get_breed())

class Cat:
    
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"

teet = Cat()    
print(teet.get_name())

brownie = Dog('mutt')
brownie._breed = ('Mutt')
print(brownie.get_breed())

class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.school_name)
print(Student.get_school_name())

class Car:
    manufacturer = "Honda"

    def __init__(self):
        self.manufacturer = "Toyota"

    def show_manufacturer(self):
        return f"{Car.manufacturer=}, {self.manufacturer=}"
    
car = Car()
print(car.show_manufacturer())

class Bird:

    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species):
        super().__init__(species)

bird = Sparrow('sparrow')
print(bird.species)

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

tom = Human()
print(tom.legs)