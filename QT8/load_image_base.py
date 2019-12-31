# Подключаем библиотеки
import sqlite3
import sys


#sqlite> CREATE TABLE Photo(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, body blob);

#sqlite> CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB);

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


try:
    # Открываем базу данных
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    # Получаем бинарные данные нашего файла
    data = readImage("woman.jpg")
    # Конвертируем данные
    binary = sqlite3.Binary(data)
    # Готовим запрос в базу
    cur.execute("INSERT INTO Photo(body) VALUES (?)", (binary,))
    # Выполняем запрос
    con.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
    cur.close()

# В случаи ошибки выводим ее текст.
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if con:
        # Закрываем подключение с базой данных
        con.close()
        print("The SQLite connection is closed")