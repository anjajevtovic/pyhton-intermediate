from pprint import pprint as pp

def add_numbers(x,y):
    return x+y

# call in another file would be:
# from modules_libraries import add_numbers
numbers = range(1,12)
sq_dict = {num:num*num for num in numbers}
pp(sq_dict)