import shutil, os
from zipfile36 import ZipFile

# Unzip
zipOutputfolder = 'archive'
fileType = 'zip'
path = r'/home/ken/Desktop/develop/projects/Python/Testdir2'
filename='test.txt'
shutil.make_archive(zipOutputfolder, fileType, path, filename)

# file to unzip
filetoUnzip = 'archive.zip'
pathToextract = r'/home/ken/Desktop/develop/projects/Python/Testdir2'
with ZipFile(filetoUnzip,'r') as zip:
    zip.printdir()

    print(os.getcwd())
    zip.extractall(pathToextract)
    print(os.getcwd())