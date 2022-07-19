# open file
myfile = open("fruits.txt")
# storing file object in variable
content = myfile.read()
# read and print file
print(myfile.read())

# file cursor
print(myfile.read())  # now gives empty as cursor is on last line

# close file
myfile.close()
