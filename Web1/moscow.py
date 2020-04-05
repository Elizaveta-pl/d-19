import json
from zipfile import ZipFile
import os
import tempfile


def read_json(file):
    with open(file) as file_r:
        reader = json.load(file_r)
        if reader['city'] == 'Москва':
            return 1
        else:
            return 0


def clear_tmp(path):
    dir = os.path.dirname(path)
    os.remove(path)
    try:
        os.removedirs(dir)
        # print("Director removed successfully")
    # Если путь не является каталогом
    except NotADirectoryError:
        pass
        # print("Specified path is not a directory.")


with ZipFile('input.zip') as archive:
    directory = tempfile.mkdtemp()
    find_key = 0
    for file in archive.namelist():

        file_info = archive.getinfo(file)
        if not file_info.is_dir() and file.split('.')[-1] == 'json':
            archive.extract(file, directory)
            if os.name == 'nt':
                file_extr = directory + '\\' + file
            elif os.name == 'posix':
                file_extr = directory + '/' + file
            find_key = find_key + read_json(file_extr)
            clear_tmp(file_extr)

    print(find_key)
