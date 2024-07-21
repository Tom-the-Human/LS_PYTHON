value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is not 1, 2, 3, 4, 5, or 6')