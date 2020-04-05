from zipfile import ZipFile
import os


def get_file_paths(source):
    # сканирование по каталогам и подкаталогам и
    file_paths = []
    file_paths1 = [os.path.join(root, filename) for root, direc, files in os.walk(source) for filename in files]

    for root, direc, files in os.walk(source):
        for filename in files:
            # объединить две строки, чтобы сформировать полный путь к файлу.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    # возвращает все пути к файлам
    print(f'file_paths = {type(file_paths)}')
    print(f'file_paths1 = {file_paths1}')
    return file_paths1


def make_reserve_arc(source, dest):
    file_name = "archive.zip"
    zipFile = ZipFile(file_name, 'w')

    file_paths = get_file_paths(source)

    with ZipFile('archive.zip', 'w') as myzip:
        for file in file_paths:
            myzip.write(file)
        # myzip.write(source)
        # print(myzip.namelist())
    pass


source = '/home/pnm/PycharmProjects/Yandex/d-19/Web1/files_zip'
dest = ''
make_reserve_arc(source, dest)
