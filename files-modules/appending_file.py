""" Wrting file with mode x """
# with open("fruits3.txt", "x") as newfile:  # gives errors if file already exists
#     newfile.write("Hello Fruits")


# appending to file
with open("fruits3.txt", "a") as appendfile:
    appendfile.write("\nAppending ")  # \n => break line

#read and write

with open("fruits3.txt", "a+") as myfile:
    myfile.write("\n adding at end")
    myfile.seek(0)  # seek cursor to start (0 poistion) of file
    print("tell =>", myfile.tell())
    print(myfile.read())
    print("tell =>", myfile.tell())
    print("seekable=> ", myfile.seekable())
    print("readable=> ", myfile.readable())
    print("writeable=> ", myfile.writable())

# Read and Append
with open("fruits2.txt", 'a+') as f:
    with open('fruits.txt', 'r') as r:
        content = r.read()
    f.write(content)

# copy n-times
with open('data.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
