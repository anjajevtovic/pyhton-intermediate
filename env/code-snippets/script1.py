a = 9
t = type(a)
print (t)
print(dir(int))
print(help(int.bit_length))

# splitting data and getting list

data = "this,is,csv,representation,of,data"
data_list = data.split(',')
print(data_list)

student1 = "Anja,127,RI"
name, index, programme = student1.split(",")
print(index)

#how to join separated data
print(": ".join(data_list))
print("".join(data_list))

#converting between types
str1 = "You are number " + str(7888)

#how to lose duplicates 
list_of_names = ["Mike", "Nina", "Anja", "Kojo", "Anja"]
set_of_names = set(list_of_names)
print(set_of_names)
get_back_to_list = sorted(set_of_names)
print(get_back_to_list)