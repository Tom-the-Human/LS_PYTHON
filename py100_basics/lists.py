def first(list_in):
    if list_in:
        return list_in[0]
    else:
        return None
    
def last(list_in):
    if list_in:
        return list_in[len(list_in) -1]
    else:
        return None

print(first([1, 2, 3]))
print(last([1, 2, 3]))
###
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

clean_energy = energy[1: len(energy)] + ['geothermal']
print(clean_energy)
###
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(list(alphabet))
###
scores = [96, 47, 113, 89, 100, 102]
count = 0
for score in scores:
    if score > 99:
        count += 1

print(count)
###
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for word_list in vocabulary:
    for word in word_list:
        print(word)
###
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, city_list):
    for city_name in city_list:
        if city_name == city:
            return True
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
###
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
finalcode = '-'.join(passcode)

print(finalcode)
###
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                 'carrots', 'broccoli', 'hummus']

while grocery_list:        #why "for" loop stop after 4?
    print(grocery_list.pop(0))

print(grocery_list)