# try:
#     num1 = float(input("Enter a number "))
#     num2 = float(input("Enter another number "))
#     result = num1 / num2
# except (ValueError, ArithmeticError) as e:
#     print("You know better than that.")
#     print(f"Original error: {type(e)}, {e}")
# else:
#     print(result)
# finally:
#     print("End of the program")
# #####

# class NegativeNumberError(ValueError):
#     pass

# num = float(input('Enter a number: '))

# if num < 0:
#     raise NegativeNumberError("Number must be positive.")
# else:
#     print(num)
# #####

# def inverse(num_list):
#     inv_list = []
#     for num in num_list:
#         try:
#             inv_list.append(1 / num)
#         except ZeroDivisionError:
#             inv_list.append(float('inf'))
#         except Exception:
#             print(f"Invalid number. {num} cannot be inverted.")
    
#     return inv_list

# print(inverse([1, 2, 3, 4.44, 500, 0.6, 0, 'zero']))
# #####

# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     return students.get(name, "Student not found.")

# print(get_age('John'))
# print(get_age('Tom'))
# #####

# numbers = [1, 2, 3, 4, 5]

# def get_6th(num_list):
#     try:
#         return num_list[5]
#     except IndexError:
#         return None
    
# def get_sixth(num_list):
#     if len(num_list) > 5:
#         return num_list[5]
#     else:
#         return None
    
# print(get_6th(numbers))
# print(get_sixth(numbers))
# #####