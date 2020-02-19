import random

# RECURSION

# LIST COMPREHENSION

list_of_names = ["Anja","Nikola","Simba"]

list_of_names_to_upper = []

for name in list_of_names:
    list_of_names_to_upper.append(name.upper())

list_of_upper_comprehension = [name.upper() for name in list_of_names]

print([num*num for num in range(6)])
print([("lenght",len(name)) for name in list_of_names])
print([f"This is {name}" for name in list_of_names])

numbers = [9, 43, 57, 50, 44]
result_list_of_numbers = [num*num for num in numbers if num%2==0]
print(result_list_of_numbers)
print(", ".join([str(num*num) for num in numbers if num%2==0]))

squares = [num*num for num in range(7)]
print(f"sum: {sum(squares)}, min: {min(squares)}, max: {max(squares)}")
print(sorted(squares, reverse=True))

lottery_numbers_string = "4, 5, 123, 10"
list_of_lottery_numbers = lottery_numbers_string.split(", ")
print(list_of_lottery_numbers)
lottery_numbers = [int(num) for num in list_of_lottery_numbers]
print(min(lottery_numbers))

# shorter version of lottery numbers
print(min([int(num) for num in lottery_numbers_string.split(", ")]))


# SET COMPREHENSION

set_of_numbers = {num*num for num in range(12)}
print(set_of_numbers)

# DICT COMPREHENSION

dict_of_numbers = {num:num*num for num in range(20)}
print(dict_of_numbers)


# GENERATOR EXPRESION (COMPREHENSIONS ARE MEMROY CONSUMING SINCE THEY ARE
# REPRODUCING WHOLE NEW LIST)
# (comprehension is going in here)
# generators cannot be reused, once you loop through them they are gone


# SLICING LISTS

my_string = "Hello, World"
print(my_string[0])
print(my_string[-1])
print(my_string[2:5])

# creationg copy of a list instead of modifying original one
names = ["claw", "quinzzy", "shapa"]
names_copy = names[:]

# to get every second one (step is the third arg)
names_copy_step = names[::2]

# getting list from backwords
names_copy_backwords = names[::-1]

# appending to names_copy will not change names list
names_copy.append("gasgas")

# ZIP function

dict_of_squares = {num:num*num for num in range(3,20,3)}
print(dict_of_squares)
print(type(dict_of_squares.keys()))

players = ["Anja","Nikola","Simba"]
scores = [100, 100, 100]
generated_zip_obj = zip(players,scores)

for item in generated_zip_obj:
    print(item)

zip_to_list = [f"{name} scored: {score}"for name, score in zip(players,scores)]
print(zip_to_list)

dict_of_zip = dict(zip(players,scores))

my_list = list(range(1,45))
rand_number = random.randint(0,100)

my_dict = {num: random.randint(0,100) for num in my_list}
print(my_dict)

# without duplicates

