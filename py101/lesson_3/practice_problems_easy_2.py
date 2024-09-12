# Question 1
numbers = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(numbers))
print(reversed_nums)
reverse_list = numbers[::-1]
print(reverse_list)

# Question 2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8
number2 = 95

print(number1 in numbers)
print (number2 in numbers)

# Question 3
def in_10_100(num):
    print(num in range(10, 101)) # Set 101 to include 100
in_10_100(42)
in_10_100(100)
in_10_100(101)

# Question 4
num_list = [1, 2, 3, 4, 5]
num_list.pop(2) # LS solution uses del numbers[2] (not sure if better)
print(num_list)

# Question 5
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers))
print(type(table))

# Question 6
title = "Flintstone Family Members"
print(title.center(40))
# Can we pass .center() something like len(table)?

# Question 7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come easy go."
print(statement1.count('t'), statement2.count('t'))

# Question 8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
print('Spot' in ages)

# Question 9
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)