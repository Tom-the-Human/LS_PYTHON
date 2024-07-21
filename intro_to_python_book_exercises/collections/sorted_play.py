name = 'Thomas W Hodges'
print(name)
print(sorted(name))
#name.sort() #doesnt work on str
#print(name)
name = list(name)
name.sort() #works when str converted to list
print(name)
name = str(name)
print(type(name), name)

name = list(name)
print(len(name), name) #interesting

