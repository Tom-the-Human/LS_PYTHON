class Bowl:
    def __init__(self, owner, usage):
        self._owner = owner
        self.usage = usage

    @property
    def owner(self):
        return self._owner
    
class MoveMixin:
    def move(self):
        print(f"{self} is moving")

class Airplane(MoveMixin):
    pass

class Planet(MoveMixin):
    pass

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am talking")

class Dog(MoveMixin, Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) # extend
        self.breed = breed

    def speak(self):
        super().speak()
        print("And i bark!")

class Husky(Dog):
    def __init__(self, name, age,):
        super().__init__(name, age, "husky")
        self.water_bowl = Bowl(self, "water")
        self.food_bowl = Bowl(self, "food")

    

bar = Animal("bar", 10)
bar.speak()
foo = Dog("foo", 5, "gsp")
# foo.move_fast()
print(foo.name)
foo.speak()
bux = Husky("bux", 5,)