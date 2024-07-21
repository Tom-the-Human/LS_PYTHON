names = ['Tom', 'Amy', 'Margot', 'Teet']
upper_names = []
#index = 0

#while index < len(names):
for name in names:
    if name != 'Margot':
        upper_name = name.upper()
        upper_names.append(upper_name)
#       index += 1



print(upper_names)