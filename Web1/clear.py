import os

razmer = {1: 'Б', 2: 'КБ', 3: 'МБ', 4: 'ГБ'}
p = []


def human_read_format(size):
    r = 1
    if size < 1024:
        return f'{size}{razmer.get(r)}'
    else:
        while size >= 1024:
            size = round(size / 1024)
            r += 1
        return f'{size}{razmer.get(r)}'


def get_files_sizes(file_paths):
    total_size = os.path.getsize(file_paths)

    return total_size


def get_directory_size(path):
    total_size = 0
    seen = set()

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                stat = os.stat(fp)
            except OSError:
                continue

            if stat.st_ino in seen:
                continue

            seen.add(stat.st_ino)

            total_size += stat.st_size

    return total_size  # size in bytes


def get_file_paths(source):
    # сканирование по каталогам и подкаталогам и создаем их список
    file_paths = {}

    for root, directs, files in os.walk(source):
        for direct in directs:
            direct = os.path.join(root, direct)
            file_paths[direct] = get_directory_size(direct)
        for filename in files:
            # объединить две строки, чтобы сформировать полный путь к файлу.
            filepath = os.path.join(root, filename)
            file_paths[filepath] = get_files_sizes(filepath)

    # возвращает все пути к файлам

    sorted_by_value = sorted(file_paths.items(), key=lambda kv: kv[1], reverse=True)
    sorted_by_value = sorted_by_value[0:10]

    for i in range(len(sorted_by_value)):
        print(f'{sorted_by_value[i][0].split("/")[-1]}  {human_read_format(sorted_by_value[i][1])}')
