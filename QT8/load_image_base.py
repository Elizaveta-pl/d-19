# Подключаем библиотеки
import sqlite3
import sys


#sqlite> CREATE TABLE Photo(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, body blob);

#sqlite> CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB);

books_jpg = ['jpg/moidodir.jpg',
            'jpg/aibolit.jpg',
            'jpg/dedmoroz.jpg',
            'jpg/kradensolnce.jpg',
            'jpg/garripotter.jpg',
            'jpg/devochkaszemli.jpg',
            'jpg/blezs.jpg',
            'jpg/ono.jpg',
            'jpg/devushkaivtumane.jpg',
            'jpg/agatakristi.jpg',
            'jpg/motilek.jpg',
            'jpg/trezorium.jpg'
            ]

# Функция открытия изображения в бинарном режиме
def readImage(filename):
    try:
        fin = open(filename, "rb")
        img = fin.read()
        return img

    # except IOError, e:
    #     # В случае ошибки, выводим ее текст
    #     print("Error %d: %s" % (e.args[0], e.args[1]))
    #     sys.exit(1)

    finally:
        if fin:
            # Закрываем подключение с файлом
            fin.close()

jpg = []
try:
    # Открываем базу данных
    # con = sqlite3.connect('catalog.db')
    # cur = con.cursor()
    for book_jpg in books_jpg:
        # Получаем бинарные данные нашего файла
        data =
        # data = readImage(book_jpg)
        # print(f'data = {data}')
        jpg.append(data)
        # Конвертируем данные
        # binary = sqlite3.Binary(data)
        # Готовим запрос в базу
        # cur.execute("INSERT INTO Photo(body) VALUES (?)", (binary,))
        # Выполняем запрос
        # con.commit()
        # print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
    # cur.close()
    print(jpg)
# В случаи ошибки выводим ее текст.
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

# finally:
#     if con:
#         # Закрываем подключение с базой данных
#         con.close()
#         print("The SQLite connection is closed")