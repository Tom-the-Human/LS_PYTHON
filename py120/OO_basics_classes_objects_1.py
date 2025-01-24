"""
1
P
Update the following code so that, instead of printing the values, 
each statement prints the name of the class to which it belongs.

1 calling print on an objec should print that object's class rather than
    the object itself
2 don't write additional code, just alter what's already here

"""



# # Comments show expected output
# print(type("Hello"))                # <class 'str'>
# print(type(5))                      # <class 'int'>
# print(type([1, 2, 3]))              # <class 'list'> 

"""
2 - 9
Create an empty class named Cat.
Using the code from the previous exercise, 
    create an instance of Cat and assign it to a variable named kitty.

    
"""
# class Cat:
    
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         self._name = name
    
#     def greet(self):
#         print(f"Hello! My name is {self.name}!")


# kitty = Cat('Sophie')
# kitty.greet()
# kitty.name = 'Luna'
# kitty.greet()

"""
10
Create a class named Person.

When you instantiate a Person object, you should 
pass in one argument that contains the person's name.

If no arguments are given, the Person object should be instantiated with 
a name of "John Doe".

"""
class Person:

    def __init__(self, name="John Doe"):
        self._name = name

    @property
    def name(self):
        return self._name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew