# 1
def select(callback, iterable):
    # output = []
    # for item in iterable:
    #     if callback(item):
    #         output.append(item)

    # return output

    return [item for item in iterable if callback(item)]

# 2
def reject(callback, iterable):
    return [item for item in iterable if not callback(item)]

# 3
def reduce(callback, iterable, start):
    accum = start
    for item in iterable:
        accum = callback(item, accum)

    return accum


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

nums = [3, 7, 2, 9, 5]
sq_sum = lambda num, accum: accum + num**2
print(reduce(sq_sum, nums, 0))