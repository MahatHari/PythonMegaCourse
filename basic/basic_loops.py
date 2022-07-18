# For Loop

monday_temp = [1.5, 2.3, 3.7, 4.7, 5.1, 6.3]
# using for x in array
for i in monday_temp:
    print(i)

# using round to round each value and print
for roundedTemp in monday_temp:
    print(round(roundedTemp))

colors = [11.3, 34.5, 98.6, 43, 45, 54, 56]
# print color if its greater than 50
for color in colors:
    if color > 50:
        print(color)

# print color if its integer
for color in colors:
    if type(color) == int:
        print(color)

# For Loop over a Function


def celcius_to_kelvin(cels):
    return cels+273.15


for temp in [9.1, 8.8, -270.15]:
    print(celcius_to_kelvin(temp))

# For Loop in Dictionaries
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

# print each dictionary values
for grades in student_grades.values():
    print(grades)
# print each dictionary keys
for student in student_grades.keys():
    print(student)

# Printing Dictionaries items as tuple
for item in student_grades.items():
    print(item)

# Dictionary Loop and String Formatting
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

# Better way to achive above result
for key, value in phone_numbers.items():
    print(f"{key} has phone number {value}")

# Replace + with 00 and print phone numbers
for phone in phone_numbers.values():
    print(phone.replace('+', '00'))

# While Loops
# while conditions: do something
a = 3
while a < 10:
    print(a)
    a += 1

username = ''
while username != "hari":
    username = input("Enter username: ")

# While loops with Break and Continue

while True:
    username = input("Enter username: ")
    if(username == 'pypy'):
        break
    else:
        continue
