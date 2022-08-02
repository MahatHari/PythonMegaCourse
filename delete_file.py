from genericpath import isfile
import os


def deletefile(file):
    if os.path.isfile(file):
        os.remove(file)


deletefile('mean.txt')
