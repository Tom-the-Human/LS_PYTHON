# 4
def later(func, argument,):
    def func_caller():
        return func(argument)

    return func_caller

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!

# 5
def later2(func, first_arg,):
    def new_func(second_arg):
        func(first_arg, second_arg)

    return new_func

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!

#####

def outer(msg='Hi!'):
    message = msg

    def inner():
        print(message) # message is a 'free variable'
        # free variables are not defined within 
        # the function but are in scope

    return inner

morning = outer('Good morning!') # now closure == inner
morning() 
# works because message was in scope when inner was defined

hi = outer()
hi()
print(hi.__closure__)

try_int = outer(10)
try_int()
print(try_int.__closure__)

#####
# Partial Function Application example
def minus(x, y):
		return x - y
		
def make_subtractor(y):
		def subtract_from(x):
				return minus(x, y)
				
		return subtract_from
		
sub10 = make_subtractor(10)
sub50 = make_subtractor(50)

print(sub50(25)) # -25
# when we call sub50, it "remembers" that y = 50
print(sub10(100)) # 90
# when we call sub10, it "remembers" that y = 10
