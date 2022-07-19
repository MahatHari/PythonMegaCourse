""" # open(file, mode='r', buffering=-1, encoding=None. errors=None, newLine=None, closedfd=True, openner=None)
# available modes r=> read, w=> truncate and wrire, x=> create new file and write, a=> open and write from end if file exist else create and write
# b=> binary mode, t=> text mode +=> open a desk file for upading(read+write) U=> universal new line(depreceated)
# Read with mode r """

with open("fruits.txt", 'r')as myfile:
    content = myfile.read()

print(content)

# Write with mode 'w', rewrite if file exist
# with open('vegetable.txt', 'w', encoding=None) as myfile:
#     myfile.write("Tomato")

with open('vegetables.txt', 'w') as myfile:
    myfile.write("Kringal\n")
    myfile.write("body\n")

# Read file and print out first 20 character of its content

with open("fruits.txt", "r") as myfile:
    content = myfile.read()
print("first 20:=> ", " ".join(content[:20]))

# File Procssing inside Function
# Function that gets a single string character and file path as paraments ad return number of occurences of that character in file


def file_processor(c, filepath):
    with open(filepath) as f:
        content = f.read()
    return content.count(c)


print(file_processor('a', "fruits.txt"))

# Write to file, 90 character from another file
with open('fruits2.txt', 'w') as f:
    with open('fruits.txt', 'r') as r:
        content = r.read()
    f.write(content[:20])
