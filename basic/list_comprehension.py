temps = [221, 234, 340, 230, -999]
new_temps = []
for temp in temps:
    new_temps.append(temp/10)

# list comprehension
new_temps1 = [temp/10 for temp in temps]

# list comprehension with conditions

new_temps2 = [temp/10 for temp in temps if temp != -999]

print("normal temps: ", new_temps)
print("Comprehension temps_ ", new_temps1)
print("Comprehension if temps: ", new_temps2)

# Only Numbers


def only_numbers(array):
    return [item for item in array if type(item) != str]


print(only_numbers(["we", 1, 2, 3, "hello", 2.3]))

# Only Poisitve numbers from array


def only_poisitive_numbers(numbers):
    return [num for num in numbers if num > 0]


print(only_poisitive_numbers([-2, -4, 2, 3, 4, 3.2]))

# Zero instead of string, condition first then for loop


def zeros_instead(para):
    return [i if not isinstance(i, str)else 0 for i in para]

# Conver and Sum up


def convert_and_sum(para):
    return sum([float(num) for num in para])
