# Working with list
monday_temp = [2.3, 8.8, 9.9]

# append
monday_temp.append(2.3)
print(monday_temp)
# clear => removes al values of list
monday_temp.clear()
print(monday_temp)  # prints [] empty array
monday_temp = [2.3, 8.8, 9.9]  # again reinitialize

# Index => return first index of a value
print(monday_temp.index(8.8))  # prints 1, index starts at 0

# Index => starts from 2
# value 8.8 starting from 2, error not on list
#print(monday_temp.index(8.8, 2))

# Acessing list Items
print(monday_temp.__getitem__(1))  # Built in method
print(monday_temp[1])

# get lenght of list
print(len(monday_temp))

# list  Slicing
print("Substring starting at 0 to 2, 0 inclusive, 2 exclusive ", monday_temp)
print(monday_temp[0:2])

# list from begingin  to 2nd
print(monday_temp[:2])

# list from 2 to end
print(monday_temp[2:])

# list negative indexing
print(monday_temp[-1])  # gives last item
# last two items using negative indexing
print(monday_temp[-2:])


# Accessing Items in Dictionaries
stu_grades = {"Mary": 4.4, "John": 3.3, "Jody": 2.2}
print(stu_grades["Jody"])


# Converting Between Datatypes

# 1. From Tuple to list
cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print("list", cool_list)

# 2. From list to tuple
back_to_tuple = tuple(cool_list)
print("tuple", back_to_tuple)

# from string to list
cool_string = "list"
string_to_list = list(cool_string)
print("list", string_to_list)

# from list to string
list_to_string = str.join("", string_to_list)

print("string", list_to_string)
list_to_string = str.join("--", string_to_list)
print(list_to_string)
