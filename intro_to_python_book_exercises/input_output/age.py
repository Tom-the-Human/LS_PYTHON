age = int(input('How old are you? '))
years = (10, 20, 30, 40)

print()
print(f'You are {age} years old.\n')

for year in years:
    print(f'In {year} years, you will be {year + age} years old.')

#print()
#print(f'You are {age} years old.\n'
#      f'In {years[0]} years, you will be {age + years[0]} years old.\n'
#      f'In {years[1]} years, you will be {age + years[1]} years old.\n'
#      f'In {years[2]} years, you will be {age + years[2]} years old.\n'
#      f'In {years[3]} years, you will be {age + years[3]} years old.\n')