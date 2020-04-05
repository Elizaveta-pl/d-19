from zipfile import ZipFile
import zipfile
# from pathlib import Path
import os


with ZipFile('input.zip') as archive:
    for file in archive.namelist():
        print(f'file = {file}')
        file_info = archive.getinfo(file)
        print(f'file_info = {file_info}')
        if file_info.is_dir():
            print(123)
            # do something

# for cont in zfile.namelist():
#     isdir = zipfile.Path.is_dir(zfile)
#     print(isdir)
#     zipfile.Path.is_dir(cont)
#     print(zipfile.Path.is_dir(zfile))
    # zfile.extract(cont,path)

with ZipFile('input.zip') as myzip:
    info = myzip.infolist()
    print(myzip.namelist())
    myzip.namelist()
    zipInfo = myzip.getinfo('files/folder2/IE11-Windows6.1-x64-ru-ru.exe')
    print(zipInfo)
    zipInfo1 = zipfile.Path.joinpath()
    print(zipInfo)

for i in myzip.namelist():
    print(i)
    zipInfo = myzip.getinfo(i)
    zipInfo1 = myzip.Path.is_dir(i)
    print(zipInfo)

    zipInfo = zipfile.Path.is_dir()
    print(zipInfo)
    if zipfile.Path.is_dir(zipInfo):
         print(f'folder =  {i}')

    ZipFile('input.zip').printdir()


# for i in range(len(info)):
#     print(f'i = {info[i].filename}')
#
#     s = info[i].orig_filename.split('/')
#
#     zipInfo = myzip.getinfo('files')
#     print(zipInfo)
#     if zipfile.Path.is_dir(info):
#         print(f'folder =  {s}')
#     if s[-1] == '':
#         print(s[-2])
#     else:
#         print(s[-1])