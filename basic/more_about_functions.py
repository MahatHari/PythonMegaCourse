# Function with  multiple Arguments

# positional argument
def area(a, b):
    return a*b


print("Area of 3l 4b is ", area(3, 4))

# Keyword arguments


def area_keyword(a, b):
    return ("a=>" + str(a) + " b=> " + str(b))


print("a is 2 b is 3", area_keyword(b=3, a=2))
print("a is 2 b is 3", area_keyword(a=2, b=3))

# default parameters


def default_para(a, b=6):
    return a*b


print("only passing a", default_para(2))
print("only passing both a and b", default_para(2, 3))

# variable length parametere


def variable_argument(*args):
    return args


print("gives tuple", variable_argument(1, 2, 3, 4, 5, 6))


# mulitple parameters
def multi_parameters(*args):
    return sum(args)/len(args)

# sorted strings of indefinite lengths


def string_indefinite(*args):
    strings_array = [string.upper() for string in args]
    return sorted(strings_array)

# keyword arguments


def mean_indefinite_arguments(**kwargs):
    return kwargs


print("As a dictionary: ", mean_indefinite_arguments(a=1, b=2, c=3))


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=1, b=2, c=3, d=3))
