my_range = range(0, 25, 3)
count = 0

for i in my_range:
    count = count + 1
    if count == 7:
        print(i)

#Ack, took the long way around for sure, 7 lines to do what can be done in 1:
#print(range(0, 25, 3)[6])
