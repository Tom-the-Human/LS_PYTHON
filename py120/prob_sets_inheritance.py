"""
1, 2
One problem is that we need to keep track of different breeds of dogs, 
since they have slightly different behaviors. For example, bulldogs 
snore when they sleep, but other dogs do not. Okay, I have no idea if that's 
entirely true; I suspect it isn't. Let's pretend it is.

Create a subclass from Dog called Bulldog overriding the sleep method to 
return "snoring!"
"""
class Pet:
    def speak():
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'
    
class Cat(Pet):
    def speak(self):
        return 'meow!'
    
class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

print(pet.run())              # running!
print(kitty.run())            # running!
print(kitty.speak())          # meow!
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(dave.speak())           # bark!

print(bud.run())              # running!
print(bud.sleep())             # "snoring!"