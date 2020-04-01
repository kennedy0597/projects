import os

# getting directories
print('os name: ', os.name)
print('os.environ: ', os.environ)
print('current working directory: ', os.getcwd())
print('directories', dir(os))
print('directories as list: ', os.listdir())
print('processor id is ', os.getpid())

# creating directory in current path
# os.mkdir("Testdir")

# change the directory to testdir
#os.chdir("Testdir")
print(os.getcwd())

# rename current directory to a different name
#os.rename("Testdir", "Testdir2")

import glob

# search *.txt and print as list to console
filelist1=glob.glob('*.py')
for list in filelist1:
    print(list)

# to fetch all directories in system exists python installation
# fetches all files responsible to run this program
import sys
for i in sys.path:
    print(i)

# to check if file exists-
if os.path.isfile('test1.txt'):
    inputfile=open('test1.txt')
    text=inputfile.readlines()
    for word in text:
        print(word)
    inputfile.close()

# shutil
import shutil

# copy test1.txt to newtest1.txt
shutil.copy('test.txt', 'newtest1.txt')
print(glob.glob('n*.txt'))

# remove a file
file_to_remove='newtest1.txt'
# os.remove(file_to_remove)
print(glob.glob('*.txt'))

# copy a foldertree
shutil.copytree('second', 'temp')
print(os.listdir())

# remove foldertree
shutil.rmtree('temp')
print(os.listdir())
