string = "canUppercaseLettersBeUsedToSplitAString"

words = string.split(char for char in string if char.isupper())

print(words)