# Creating function in Pythong
from tkinter.tix import Y_REGION


def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean


print("Mean of given array", mean([1, 2, 3, 4]))
# type
print(type(sum), type(mean))

# Conditionals


def meanConditions(input):
    if type(input) == dict:  # if isinstance(value, dict) => also checks for dict
        the_mean = sum(input.values())/len(input)
    else:
        the_mean = sum(input)/len(input)
    return the_mean


print("Dictionary", meanConditions({"John": 2, "Mary": 5, "Sia": 10}))
print("List", meanConditions([2, 3, 4, 5]))


# and or in python
x = 1
y = 2
if x == 1 and y == 2:
    print(True)
else:
    print(False)

if x == 1 or y == 2:
    print("Or True")
else:
    print("Or false")

# Elif conditionals
if x > y:
    print("Greter")
elif x < y:
    print("Smaller")
else:
    print("Equal")
