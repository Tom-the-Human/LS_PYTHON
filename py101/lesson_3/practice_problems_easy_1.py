# Question 1 - Yes, out of index

# Question 2
str1 = "Come over here!"
str2 = "What's up Doc?"

for phrase in [str1, str2]:
    if phrase[-1] == "!":
        print(True)
    else:
        print(False)

# Question 3
famous_words = "seven years ago..."
more_famous_words = "Four score and " + famous_words
prepend = "Four score and "
extra_words = prepend + famous_words
new_string = f'Four score and {famous_words}'
print(more_famous_words)
print(new_string)

# Question 4
munsters_description = 'the Munsters are CREEPY and Spooky.'
fix_caps = munsters_description.capitalize()
print(fix_caps)

# Question 5
reverse_caps = fix_caps.swapcase()
print(reverse_caps)

# Question 6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print(("Dino" in str1))
print(("Dino" in str2))

# Question 7 & 8
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)

# Question 9
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("house training your pet dinosaur.", ""))
print(advice.split("house")[0])

# Question 10
print(advice.replace("important", "urgent"))