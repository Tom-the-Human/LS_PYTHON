# class InvoiceEntry:
#     def __init__(self, product_name, number_purchased):
#         self._product_name = product_name
#         self._quantity = number_purchased

#     @property
#     def quantity(self):
#         return self._quantity
    
#     @quantity.setter
#     def quantity(self, quantity):
#         self._quantity = quantity

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000
# #####

# class Animal:
#     def speak(self, sound):
#         print(f"{sound}")

# class Cat(Animal):
#     def __init__(self):
#         pass

#     def meow(self):
#         self.speak('Meow!')

# class Dog(Animal):
#     def bark(self):
#         self.speak('Woof! ' * 3)

# teet = Cat()
# brownie = Dog()
# teet.meow()
# brownie.bark()
# #####

# class KrispyKreme:
#     def __init__(self, filling, glazing):
#         self.filling = filling
#         self.glazing = glazing

#     def __str__(self):
#         filling = self.filling
#         glazing = self.glazing

#         if filling and glazing:
#             donut = f'{filling} with {glazing}'
#         elif filling and (not glazing):
#             donut = f'{filling}'
#         elif (not filling) and glazing:
#             donut = f'Plain with {glazing}'
#         else:
#             donut = f'Plain'

#         return donut

# donut1 = KrispyKreme(None, None)
# donut2 = KrispyKreme('Vanilla', None)
# donut3 = KrispyKreme(None, 'sugar')
# donut4 = KrispyKreme(None, 'chocolate sprinkles')
# donut5 = KrispyKreme('Custard', 'icing')

# print(donut1)       # Plain
# print(donut2)       # Vanilla
# print(donut3)       # Plain with sugar
# print(donut4)       # Plain with chocolate sprinkles
# print(donut5)       # Custard with icing
# #####

