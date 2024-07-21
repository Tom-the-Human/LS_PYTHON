car = {
    'type': 'sedan', 
       'color': 'blue', 
       'mileage': 80_000
}

car['year'] = 2003

del car['mileage']

print(len(car))
###
student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)
print('grade' in student)
###
vehicle = {
    'Car': {
        'type': 'sedan', 
    'color': 'blue', 
    'year': 2003
    },
    'Truck': {
        'type': 'pickup', 
        'color': 'red',
        'year': 1998
        }
}
###
car = [
    ['type', 'sedan'], 
    ['color', 'blue'], 
    ['year', 2003]
]
###
numbers = {
    'high':     100,
    'medium':   50,
    'low':      25,
}

half_numbers = []
for num in numbers.values():
    half_numbers.append(int(num / 2))

print(half_numbers)

numbers2 = {
    'high':     100,
    'medium':   50,
    'low':      10,
}

for num in numbers2:
    print(f'A {num} number is {numbers2[num]}.')