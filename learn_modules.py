import time  # import time module
import os  # import os module

while True:
    if os.path.exists('files/vegetables.txt'):
        with open('fruits.txt') as file:
            print(file.read())
            time.sleep(10)  # using module with . notation
    else:
        print("File does not exist")
    break
