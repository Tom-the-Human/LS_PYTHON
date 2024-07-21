def rangefinder(number):
    if (number >= 0) and (number < 51):
        print(f'{number} is between 0 and 50')
    elif (number >= 51) and (number < 101):
        print(f'{number} is between 51 and 100')    
    elif (number >= 101):
        print(f'{number} is greater than 100')
    elif (number < 0):  #probably more readable if this is first condition
        print(f'{number} is less than 0')
    else:   
        print('error')    


number = int(input('Enter a number: '))
rangefinder(number)