# Variable
spend = 3
donated = 4
total_amount = spend + donated
print(total_amount)

#string and number
# Integer are used to represent whole numbers:
rank = 10
eggs = 12,

# Floats represent decimal numbers
temp = 10.2
rainfall = 2.3
elevation = 23.2
# String represent text
message = "Hello World"
name = "Hary"

x = 10
y = "10"
sum1 = x + int(y)
sum2 = y + str(x)
print(sum1, sum2)

# Lists represents array of values that may change during the course of program
mixed_list = [9, 19.3, "hello", [1, 2, 3]]
piex_values = [222, 233, 244, 255, 4334]
print(mixed_list)

print(mixed_list*3)


# list range
automated_list = list(range(0, 10))  # inclusive 0, exclusive 10
automated_list_step = list(range(0, 11, 2))
print(automated_list)

# Data Types
# 1. List
# dir(list) => shows all that list methods
# help(methodName) => shows what method does
# dir(__builtins__) => complete list of built in function
# Calulate average
grades = [1, 3, 4, 6, 2, 6, 2, ]
mysum = sum(grades)
length = len(grades)
mean = mysum/length
print(mean)

# Get max value out of iterable (list)
max_value = max(grades)
print(max_value)

# Count Values, count a specific numbers inside of list
print(grades.count(6))

# Dictionary  represent pairs of keys and vlues
stu_grades = {"Mary": 3, "John": 4, "Jeus": 35}
phone_numers = {"sim": 12321323423, "kim": 2342234234, "simon": 2342342}
# values of dictionary can be extracted with
print(stu_grades.values())  # prints list of values
# keys of dictionary can be extracted with
print(stu_grades.keys())  # prints list of keys

# print key-> value
print(stu_grades["Mary"])

# Tuples => immutable, dont have add or remove methods
monday_temp = (1, 4, 5)
print(monday_temp)

# You can get a list of attributes of data type using
dir(str)
dir(list)
dir(dict)


# You can get lis of Python builtin functions using:
dir(__builtins__)

# You cn get documentation of Python data type using
help(str)
help(str.replace)
help(dict.values)
