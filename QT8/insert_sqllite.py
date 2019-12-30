import sqlite3
import sys


try:
    genres = ['Детективы', 'Приключения', 'Фантастика', 'Фэнтези', 'Стихи']
    where_sql = 'title'
    where_sql_text = ''
    # Открываем базу данных
    con = sqlite3.connect('catalog.db')
    cur = con.cursor()
    # Получаем бинарные данные нашего файла
    # data = readImage("woman.jpg")
    # # Конвертируем данные
    # binary = sqlite3.Binary(data)

    # Готовим текст запроса в базу
    text_sql = f'INSERT INTO Photo(body)  WHERE {where_sql} = {where_sql_text}'
    for genre in  genres:
        text_sql = f'INSERT INTO genres(title) VALUES ({genre})'
        print(text_sql)
        # Готовим запрос в базу
        # cur.execute()
        result = cur.execute(text_sql)
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