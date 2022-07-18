# Handling User Inputs
# commanline input
def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


user_input = input("Enter Temperature: ")  # input is string
# changing input to float
user_input = float(user_input)

# can be writting in single line
# user_input= float(input("Enter temperature: "))
print(weather_condition(user_input))

user_input = input("Enter your name: ")
# String formatting
message1 = "Hello %s" % user_input

# String formatting, above version 3.6
message2 = f"hello {user_input}"
print(message1)
print(message2)

fname = input("Enter first name: ")
lname = input("Enter last name: ")

message3 = "Hello %s %s" % (fname, lname)
print(message3)

message4 = f"Hello {fname} {lname}"
print(message4)

# String formatting with .format(values)
message5 = "Your name is {}, Your surname is {}".format(fname, lname)
print(message5)


def person(name):
    capital = name[0].upper()
    cap_name = capital+(name[1:])
    return f"Hi {cap_name}"
