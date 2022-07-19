import pandas
import os
import sys

# using external module pandas, for reading csv file
while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data)
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    break

print("Built in Module Names ")
for name in sys.builtin_module_names:
    print(name)
