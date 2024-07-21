my_list = [6, 3, 0, 11, 20, 4, 17]
i = 0

while i < len(my_list):
    if i % 2 == 0:
        print(my_list[i])
    i += 1

for item in my_list:
    if item % 2 == 1:
        print(item)    
###

list2 = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0]
]

list3 = []

for inner_list in list2:
    for num in inner_list:
        if num % 2 == 0:
            list3.append('even')
        if num % 2 != 0:
            list3.append('odd')
print(list3)
###

def find_integers(tup):
    return [ element
            for element in tup
            if type(element) is int ]
        
my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
print(find_integers(my_tuple))
###

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

pet_dict = { name: len(name)
            for name in my_set
            if len(name) % 2 != 0 }
print(pet_dict)
###

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    
    return result
print(factorial(4))
###

last_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

i = 0
j = 0

while i < len(last_list): 
    if j < len(last_list[i]):
        curr_num = last_list[i][j]
        if curr_num % 2 == 0:
            print(curr_num)
        j +=1
    else:  
        j = 0
        i += 1

    

        
