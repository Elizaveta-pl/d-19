import random
g = list(open("lines.txt"))
if len(g) != 0:
    d = random.randrange(0, (len(g) - 1))
    print(g[d])
else:
    print('')

    # Модифицируйте
    # программу «Случайная
    # строка
    # из
    # файла».Напишите
    # для
    # нее
    # интерфейс
    # на
    # PyQT.Выводите
    # случайную
    # строку
    # из
    # файла
    # в
    # подходящий
    # для
    # этого
    # виджет.