"""
1
Create a class named Cat for which 
calling Cat.generic_greeting prints Hello! I'm a cat!.
"""
# class Cat:
#     @classmethod
#     def generic_greeting(cls):
#         print("Hello! I'm a cat!")

# Cat.generic_greeting()
# kitty = Cat()
# kitty.generic_greeting()
# type(kitty).generic_greeting()
# # type() returns the class of the argument

"""
2
Using the following code, add an instance method named rename 
that renames kitty when invoked.
"""
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     def rename(self, value):
#         self.name = value

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.name)             # Sophie
# kitty.rename('Chloe')
# print(kitty.name)             # Chloe

"""
3
Using the following code, add a method named identify 
that returns the calling object.
"""
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     def identify(self):
#         return self

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.identify())
# # <__main__.Cat object at 0x10508c8d0>
# # The object ID (0x105...) may vary

"""
4
Using the following code, add a personal_greeting method 
that prints a message as shown below:
"""
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     def personal_greeting(self):
#         print(f'Hello! My name is {self.name}')

# kitty = Cat('Sophie')
# kitty.personal_greeting()     # Hello! My name is Sophie!

"""
5
Create a class named Cat that tracks the number of times a new Cat object is 
instantiated. The total number of Cat instances should be printed when 
total is invoked.
"""
# class Cat:
#     objects = 0

#     def __init__(self):
#         Cat.objects += 1

#     @classmethod
#     def total(cls):
#         print(cls.objects)


# Cat.total()         # 0

# kitty1 = Cat()
# Cat.total()         # 1

# kitty2 = Cat()
# Cat.total()         # 2

# print(Cat())        # <__main__.Cat object at 0x104ed7290>
# Cat.total()         # 3

"""
6
Create a class named Cat that prints a greeting when the greet instance 
method is invoked. The greeting should include the name and color of the 
cat. Use a class constant to define the color.
"""
# class Cat:
#     COLOR = "purple"

#     def __init__(self, name):
#         self.name = name
#         self.color = Cat.COLOR

#     def greeting(self):
#         print(f"Hello! My name is {self.name} and I'm a {self.color} cat!")

# kitty = Cat("Sophie")
# kitty.greeting()

"""
7
Update the following code so that it prints I'm Sophie! 
when it invokes print(kitty).
"""
class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return f"I'm {self.name}!"
    


# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!
