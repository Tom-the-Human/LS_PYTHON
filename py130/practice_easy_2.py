# # 1
# def greet(name, greeting, punctuator='.'):
#     return f"{greeting}, {name}{punctuator}"

# print(greet("Tom", "Hey",))
# print(greet("Tom", "You're really good at this", "!"))

# # 2
# def create_user(username, *, email, age):
#     return {"username": username, "email": email, "age": age}

# print(create_user("Srdjan", email="srdjan@example.com", age=39))
# # {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
# print(create_user("Srdjan", "srdjan@example.com", age=39))
# # Raises an exception

# # 3
# def build_profile(first, last, **kwargs):
#     profile = {"first_name": first, "last_name": last, }
#     for key, value in kwargs.items():
#         profile[key] = value

#     return profile

# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# # {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

# # 4
# def concatenate(*strings):
#     return ' '.join(strings)

# print(concatenate("Launch", "School", "is", "great")) # Launch School is great
# print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

# # 5
# def display_info(data, /, *, reverse=False, uppercase=False):
#     if uppercase:
#         data = data.upper()
#     if reverse:
#         data = data[::-1]
    
#     return data

# print(display_info("Launch", reverse=True)) # hcnuaL
# print(display_info("School", uppercase=True)) # SCHOOL
# print(display_info("cat", uppercase=True, reverse=True)) # TAC

# # 6
# lst = [10, 20, 30, 40]
# a, b, c, d = lst
# print(a, b, c, d)

# # 7
# data = (100, 200, 300, 400)
# first, *_, last = data
# print(first, last)

# # 8
# numbers = [1, 2, 3, 4, 5, 6]
# one, two, *rest = numbers
# print(one, two, rest)

# # 9
# data = ((1, 2), (3, 4), (5, 6))
# a, b, c, d, e, f = tuple(obj for subtup in data for obj in subtup)
# print(a, b, c, d, e, f)