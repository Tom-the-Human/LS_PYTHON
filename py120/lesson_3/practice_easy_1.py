# class AngryCat:
#     def hiss(self):
#         print('Hisssss!!!')

# margot = AngryCat()
# margot.hiss()
# #####

# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}')

# class Car(SpeedMixin):
#     def go_slow(self):
#         print('I am safe and driving slow.')

# class Truck(SpeedMixin):
#     def go_very_slow(self):
#         print('I am a heavy truck and like going very slow.')

# car = Car()
# car.go_fast()
# print(car.__class__.mro())

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
margot = Cat('mean')
teet = Cat('nice')
print(Cat.cats_count())
