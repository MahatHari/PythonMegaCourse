
# open file using with method, close is not required as with closes
with open("fruits.txt") as myfile:
    content = myfile.read()
print(content)


# different file paths

with open("../basic/basic_program.py") as myfile:
    content = myfile.read()
print(content)
