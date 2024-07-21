people = ['Amy', 'Tom', 'Felix']
print(len(people))


stuff = ('hello', 'world', 'bye', 'now')
stufflist = list(stuff)
stufflist[2] = 'goodbye'
stuff = tuple(stufflist)
print(stuff)

pi = 3.141592
str_pi = str(pi)
print(type(str_pi), str_pi)

old_tup = (1, 2, 3, 4, 5)
sort_list = list(old_tup)
sort_list.reverse()
new_tup = tuple(sort_list[1:4])
print(new_tup)

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

info = 'Thomas Warfield Hodges'
result = info.replace('o', '0')
result = result.replace('a', '@')
result = result.replace('d', 'th')
result = result.replace('Th0m@s W@rfielth', 'Amy Rose')
print(result)