# class GoodDog:
    
#     def __init__(self, name):
#         self.name = name
#         print(f'Constructor for {self.name}')

#     def speak(self):
#         print(f'{self.name} says Woof!')

#     def up_up(self):
#         print(f'{self.name} stands on hind legs.')


# teet = GoodDog('Teet')
# teet.speak()
# teet.up_up()

# margot = GoodDog('Margot')
# margot.speak()
# margot.up_up()
#######################################


# class Pet:

#     def __init__(self, name):
#         self.name = name
#         type_name = type(self).__name__
#         print(f'I am {name}, a {type_name}.')

#     def eat(self):
#         print(f'{self.name}: Yum!')

# class Dog(Pet):

#     # __init__ method removed
#     def speak(self):
#         print(f'{self.name} says Woof!')

#     def roll_over(self):
#         print(f'{self.name} is rolling over.')

# class Cat(Pet):

#     # __init__ method removed
#     def speak(self):
#         print(f'{self.name} says Meow!')

# class Parrot(Pet):

#     # __init__ method removed
#     def speak(self):
#         print(f'{self.name} wants a cracker!')

# sparky = Dog('Sparky')
# fluffy = Cat('Fluffy')
# polly = Parrot('Polly')

# sparky.roll_over()

# for pet in [sparky, fluffy, polly]:
#     pet.speak()
#     pet.eat()
#######################################

# class Pizza:

#     def __init__(self, kind, minutes):
#         self.kind = kind
#         self.cook_minutes = minutes
#         self.type_name = self.__class__.__name__

#     def cook_time(self):
#         print(f'We need a {self.kind} pizza for {self}.')
#         print(f'A {self.kind} pizza takes {self.cook_minutes} minutes to cook.')

#     def say_what(self):
#         print(f'I am a {self.type_name} object.')

#     def say_again(self):
#         print(f'I am a {str(type(table1).__name__).lower()} object.')

# table1 = Pizza('pepperoni', 21)

# table2 = Pizza('margherita', 17)

# table1.cook_time()
# table1.say_what()
# table1.say_again()

# table2.cook_time()
#######################################

# class GoodDog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         return f'{self.name} says "Arf!"'
    
#     def _dog_years(self):
#         return self._age * 7
    
#     def show_age(self):
#         print(f'My age in dog years is {self._dog_years()}.')

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('Name must be a string')
        
#         self._name = name

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, age):
#         if not isinstance(age, int):
#             raise TypeError('Age must be an integer')
        
#         if age < 0:
#             raise ValueError("Age can't be negative")
        
#         self._age = age
    
    

# sparky = GoodDog("Sparky", 5)
# #print(sparky._GoodDog._name)  #!
# print(sparky.speak())

# rover = GoodDog("Rover", 3)
# print(rover.speak())


# print(sparky.name)
# sparky.name = 'Fireplug'
# print(sparky.name)

# print(sparky.age)
# sparky.age = 7
# print(sparky.age)

# sparky.name = '100'
# rover.age = abs(-5)

#######################################

# class Car:

#     def __init__(self, model, year, color):
#         self._model = model
#         self._year = year
#         self._color = color
#         self.curr_speed = 0

#     @property
#     def color(self):
#         print(f'The {self._model} is {self._color}.')

#     @color.setter
#     def color(self, color):
#         if not isinstance(color, str):
#             print('Color must be a string!')

#         self._color = color

#     def respray(self, color):
#         self._color = color
#         print(f'The {self._color} paint looks great!')


#     @property
#     def model(self):
#         print(f'This vehicle is a {self._model}.')

#     @property
#     def year(self):
#         print(f'The {self._model} is a {self._year}.')

#     @classmethod
#     def avg_mpg(cls, miles, gallons):
#         print(f'This vehicle gets about {miles // gallons}mpg.')

#     def engine_start(self):
#         print(f'You start the {self._model}.')

#     def accelerate(self):
#         print(f'You accelerate the {self._model} by 10mph.')
#         self.curr_speed += 10

#     def brake(self):
#         print(f'You brake, slowing the {self._model} by 10mph.')
#         self.curr_speed -= 10

#     def engine_off(self):
#         print(f'You turn off the {self._model}.')
#         self.curr_speed = 0

#     def get_speed(self):
#         print(f'Current speed is {self.curr_speed}.')

# pickup = Car("F150", 2021, "blue")
# pickup.engine_start()
# pickup.accelerate()
# pickup.get_speed()
# pickup.accelerate()
# pickup.accelerate()
# pickup.get_speed()
# pickup.brake()
# pickup.get_speed()
# pickup.engine_off()
# pickup.get_speed()
# pickup.color
# pickup.color = 'black'
# pickup.color
# pickup.model
# pickup.year
# pickup.respray('polkadot')
# pickup.color
# Car.avg_mpg(267, 11)

#######################################

# class Person:

#     def __init__(self, first, last):
#         if first.isalpha() and last.isalpha():
#             self._first = first.capitalize()
#             self._last = last.capitalize()
#         else:
#             print('Names must be strings of letters only!')
        
#     @property
#     def name(self):
#         return f"{self._first} {self._last}"

#     @name.setter
#     def name(self, name_tup):
#         if name_tup[0].isalpha() and name_tup[1].isalpha():
#             self._first = name_tup[0].capitalize()
#             self._last = name_tup[1].capitalize()
#         else:
#             print('Names must be strings of letters only!')

# friend = Person('Lynn', 'Blake')
# print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# # ValueError: Name must be alphabetic.

#######################################

# import os

# print(__file__)
# print(os.path.abspath(__file__))

#######################################

# class Car:
#     def __init__(self, id, year, color):
#         self.id = id
#         self.year = year
#         self.color = color

#     def __str__(self):
#         return f'{self.color.capitalize()} {self.year} {self.id}'
    
#     def __repr__(self):
#         return f'Car({repr(self.id)}, {repr(self.year)}, {repr(self.color)})'


# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

#######################################

# from math import sqrt

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     # __iadd__ method omitted; we don't need it for this exercise

#     def __sub__(self, other):
#         new_x = self.x - other.x
#         new_y = self.y - other.y

#         return Vector(new_x, new_y)
    
#     def __mul__(self, other):
#         new_x = self.x * other.x
#         new_y = self.y * other.y

#         return new_x + new_y
    
#     def __abs__(self):
#         return sqrt(self.x**2 + self.y**2)

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)

# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

#######################################

# class Candidate:

#     def __init__(self, name):
#         self.name = name
#         self.votes = 0

#     def __iadd__(self, other):
#         self.votes += other
#         return self

# class Election:

#     def __init__(self, candidates):
#         self.candidates = candidates

#     def results(self):
#         most_votes = 0
#         vote_count = 0
#         winner = None

#         for candidate in candidates:
#             vote_count += candidate.votes
#             if candidate.votes > most_votes:
#                 most_votes = candidate.votes
#                 winner = candidate.name

#         for candidate in candidates:
#             name = candidate.name
#             votes = candidate.votes
#             print(f'{name}: {votes} votes')

#         percent = 100 * (most_votes / vote_count)
#         print()
#         print(f'{winner} won: {percent}% of votes')


# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()

# print(Candidate.mro())

#######################################

# Write the code needed to make the following code work as shown:

# class SignalMixin:

#     def signal_left(self):
#         print('Signalling left')

#     def signal_right(self):
#         print('Signalling right')

#     def signal_off(self):
#         print('Signal is now off')

# class Vehicle:

#     vehicle_count = 0

#     def __init__(self):
#         Vehicle.vehicle_count += 1

#     @classmethod
#     def vehicles(cls):
#         return Vehicle.vehicle_count
    
# class Car(SignalMixin, Vehicle,):

#     def __init__(self):
#         super().__init__()

# class Truck(Vehicle, SignalMixin):
    
#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle):

#     def __init__(self):
#         super().__init__()




# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# # boat1.signal_left()
# # AttributeError: 'Boat' object has no attribute
# # 'signal_left'

# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro())

#######################################

class Vehicle:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car