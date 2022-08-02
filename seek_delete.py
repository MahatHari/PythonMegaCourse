import glob
import os

files = glob.glob('*.txt')

for file in files:
    with open(file) as f:
        content = f.read().lower()
    if 'xxx' in content:
        os.remove(file)
