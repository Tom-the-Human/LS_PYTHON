def caps_if_10plus(str_in): #misread directions(should be caps_if_over_10)
    if len(str_in) >= 10:   #this expresses same function, though not same result
        return str_in.upper()
    else:
        return(str_in)

str_in = input('Enter text string: ')
print(caps_if_10plus(str_in))