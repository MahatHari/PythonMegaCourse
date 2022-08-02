import glob
import os

text_files = glob.glob('*.txt')
i = 1
for files in text_files:
    os.rename(files, 'file-'+str(i)+'.txt')
    i += 1
