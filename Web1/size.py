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


def get_files_sizes():
    print(os.listdir())
    for i in os.listdir():
        if os.path.isfile(i):
            p.append(i + ' ' + human_read_format(os.path.getsize(i)))
    return('\n'.join(p))


print(get_files_sizes())