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