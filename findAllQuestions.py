import re

with open('fil2.txt') as f:
    content = f.read()
    print(re.findall("[A-Z][a-z ' ,]*\?", content))


# string formatting, Dictionary Format
names = {"firstname": "Andy", "lastname": "Smith"}
print("Welcome {firstname} {lastname} to our shop!".format(**names))

# A.S
# Fill in the two {} brackets so that the output of the code is Welcome A.S to our shop!

firstname = "Andy"
lastname = "Smith"
print("Welcome {:.1}.{:.1} to our shop!".format(firstname, lastname))
