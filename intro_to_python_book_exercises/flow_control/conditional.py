value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is not 3 or 4')

print(value == 4 or 3) 
#why does [or] not work as expected here? 
#4 evaluates True, 3 evaluates 3 ???
print((3 or 4) == value)
#always False
print(True if (value == 3 or 4) else False)
#always True
print((value == 3) or (value == 4))
#this works as expected!