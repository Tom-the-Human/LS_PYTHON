"""
1
Complete this class so that the test cases shown below work as intended. 
You are free to add any methods or instance variables you need. However, 
methods prefixed with an underscore are intended for internal use and should 
not be called externally.

You may assume that the input will always fit in your terminal window.
"""
# class Banner:
#     def __init__(self, message):
#         self._message = message

#     @property
#     def message(self):
#         return self._message
    
#     @message.setter
#     def message(self, message):
#         self._message = message

#     def __str__(self):
#         return "\n".join([self._horizontal_rule(),
#                           self._empty_line(),
#                           self._message_line(),
#                           self._empty_line(),
#                           self._horizontal_rule()])

#     def _empty_line(self):
#         return "| " + (" " * len(self.message)) + " |"

#     def _horizontal_rule(self):
#         return "+-" + ("-" * len(self.message)) + "-+"

#     def _message_line(self):
#         return f"| {self.message} |"


# # Comments show expected output

# banner = Banner('To boldly go where no one has gone before.')
# print(banner)
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# banner = Banner('')
# print(banner)
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+

"""
2
Create a Rectangle class whose initializer takes two arguments that 
represent the rectangle's width and height, respectively. Use the 
following code to test your solution:
"""
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = self.width * self.height

# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

"""
3
Write a class called Square that inherits from the Rectangle class. 
The Square class is used like this:
"""
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height
    
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
    
# square = Square(5)
# print(square.area == 25)      # True

"""
4
Update this code so you see the following output when you run the code:
"My cat Cocoa is 3 years old and has black fur."
"My cat Cheddar is 4 years old and has yellow and white fur."
"""
# class Pet:
#     def __init__(self, name, age, color):
#         self._name = name
#         self._age = age
#         self._color = color

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age
    
#     @property
#     def color(self):
#         return self._color
    
#     def info(self):
#         return f"My pet {self.name} is {self.age} years old and has {self.color} fur."

# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age, color)

#     @property
#     def info(self):
#         return f"My cat {self.name} is {self.age} years old and has {self.color} fur."

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)

"""
5
Given the following Animal class, create two more classes, 
Cat and Dog, that inherit from it:
The Cat initializer should accept 3 parameters: name, age, and status. 
Cats should always have a leg count of 4 and a species of "cat". 
The introduce method for the Cat class should return a string identical to 
the base class with an added Meow meow! at the end. For example:
The Dog initializer should accept 4 parameters: name, age, status, and owner. 
Dogs should always have a leg count of 4 and a species of "dog". 
In addition to the methods inherited from Animal, the Dog class should have a 
greet_owner method that returns a greeting to its owner followed by 
Woof! Woof!. The introduce method for the Dog class should return a string 
identical to the base class with an added Woof! Woof! at the end.
"""
# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")
    
# class Cat(Animal):
#     def __init__(self, name, age, status):
#         super().__init__(name, age, 4, "cat", status)

#     def introduce(self):
#         return super().introduce() + " Meow meow!"
    
# class Dog(Animal):
#     def __init__(self, name, age, status, owner):
#         super().__init__(name, age, 4, "dog", status)
#         self.owner = owner

#     def greet_owner(self):
#         return f"Hi {self.owner}! Woof! Woof!"
    
#     def introduce(self):
#         return super().introduce() + " Woof! Woof!"
    
# cat = Cat("Pepe", 4, "happy")
# expected = ("Hello, my name is Pepe and I am 4 years old "
#             "and happy. Meow meow!")
# print(cat.introduce() == expected)      # True

# dog = Dog("Bobo", 9, "hungry", "Daddy")
# expected = ("Hello, my name is Bobo and I am 9 years old "
#             "and hungry. Woof! Woof!")
# print(dog.introduce() == expected)                  # True
# print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True

"""
6
Write the classes and methods that will be necessary to make this code run, 
and log the following output:
P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
"""
# class Pet():
#     def __init__(self, species, name):
#         self.species = species
#         self.name = name

#     def info(self):
#         return f'a {self.species} named {self.name}'

# class Owner():
#     def __init__(self, name):
#         self.name = name
#         self.pets = []

#     def number_of_pets(self):
#         return len(self.pets)
    
#     def __str__(self):
#         return self.name

# class Shelter():
#     def __init__(self):
#         self.owners = set()

#     def adopt(self, owner, pet):
#         owner.pets.append(pet)
#         self.owners.add(owner)

#     def print_adoptions(self):
#         for owner in self.owners:
#             print(f"{owner} has adopted the following pets:")
#             for pet in owner.pets:
#                 print(pet.info())


# cocoa   = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin  = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly   = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")

"""
7
Refactor these classes so the all use a common superclass 
and inherit behavior as needed.
"""
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def get_wheels(self):
#         return 4

#     def info(self):
#         return f"{self.make} {self.model}"
    
# class Car(Vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)

# class Motorcycle(Vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)

#     def get_wheels(self):
#         return 2

# class Truck(Vehicle):
#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

#     def get_wheels(self):
#         return 6

"""
8
You have the following classes.
You need to modify the code so that this works:
You may only write one new method to do this.
"""
# class WalkMixin:
#     def walk(self):
#         if isinstance(self, Noble):
#             return f"{self.title} {self.name} {self.gait()} forward"
        
#         return f"{self.name} {self.gait()} forward"
    
# class Person(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

# class Cat(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(Cat):
#     def __init__(self, name):
#         super().__init__(name)

#     def gait(self):
#         return "runs"
    

# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

"""
9
Now that we have a WalkMixin mix-in, we are given a new challenge. 
Apparently some of our users are nobility, and the regular way of walking 
simply isn't good enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called. 
We also require access to name and title; they are needed for other purposes 
that we aren't showing here.
"""
# class Noble(Person):
#     def __init__(self, name, title):
#         super().__init__(name)
#         self.title = title

#     def gait(self):
#         return "struts"

# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)    # "Byron"
# print(byron.title)   # "Lord"

"""
10
Modify the House class so the above program works as shown.
"""
# class House:
#     def __init__(self, price):
#         self._price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     def __gt__(self, other):
#         return self.price > other.price
    
#     def __lt__(self, other):
#         return self.price < other.price

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

"""
11
Implement a Wallet class that represents a wallet with a certain amount 
of money. You want to be able to combine (add) two wallets together to get 
a new wallet with the combined total amount from both wallets.

12
Using the code from the previous exercise, modify the code so that when we 
print the merged_wallet we receive a message Wallet with $80.
"""
# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Wallet(self.amount + other.amount)
    
#     def __str__(self):
#         return f"Wallet with ${self.amount}."

# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.amount == 80)       # True
# print(merged_wallet)          # Wallet with $80.

"""
13
Write a class such that the following code prints the 
results indicated by the comments:
"""
# class Transform:
#     def __init__(self, text):
#         self.text = text

#     def uppercase(self):
#         return self.text.upper()
    
#     @classmethod
#     def lowercase(cls, text):
#         return text.lower()

# my_data = Transform('abc')
# print(my_data.uppercase())              # ABC
# print(Transform.lowercase('XYZ'))       # xyz

