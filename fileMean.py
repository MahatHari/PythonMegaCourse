import glob
import re

text_files = glob.glob("*.txt")
lst = []
for files in text_files:
    with open(files) as f:
        lst.append((f.readlines()))

all_lines = sum(lst, [])


matches = [re.compile('[0-9]+\.*[0-9]*').search(line) for line in all_lines]
numbers = [float(match.group(0)) for match in matches if match]

with open('mean.txt', 'a') as file:
    file.write(str(sum(numbers)/len(numbers)))
