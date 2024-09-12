# Question 1
def add_hyphen(string):
    return("-" + string)
flintstones = "The Flintstones Rock!"
for i in range(1, 11):
    print(add_hyphen(flintstones))
    flintstones = add_hyphen(flintstones)

# Question 2
def factors(number):
    if number < 0:
        return "Negative values not allowed"
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
print(factors(-8))
# 'while divisor > 0' is definitely cleaner than my solution,
# but I think a message should be returned if number is negative.

# No remaining questions require coding
