import sqlite3
import sys


try:
    genres = ['Детективы', 'Романы', 'Фантастика', 'Фэнтези', 'Стихи']
    books = [['Мойдодыр', 'Чуковский Корней', 2016, 5, 1],
            ['Айболит', 'Чуковский Корней', 2015, 5, 2],
            ['Дед Мороз', 'Степанов В.', 2017, 5, 3],
            ['Краденое солнце', 'Жигарев Вячеслав Алексеевич', 2010, 5, 4],
            ['Гарри Поттер', 'Роулинг Джоан Кэтлин', 2018, 4, 5],
            ['Девочка с Земли', 'Кир Булычев', 2016, 4, 6],
            ['Блейз', 'Кинг Стивен', 2018, 3, 7],
            ['Оно. Тень прошлого', 'Кинг Стивен', 2018, 3, 8],
            ['Девушка в тумане', 'Карризи Донато', 2018, 1, 9],
            ['Убийства по алфавиту', 'Кристи Агата', 2019, 1, 10],
            ['Мотылек', 'Шарьер Анри', 2015, 2, 11],
            ['Трезориум', 'Борис Акунин', 2019, 2, 12]
            ]
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

    text_sql_genres = f'INSERT INTO genres VALUES (?,?)'
    text_sql_book = f'INSERT INTO book VALUES (?,?,?,?,?,?)'
    # for i, genre in enumerate(genres):
    #      # Готовим запрос в базу
    #     cur.execute(text_sql_genres, (i+1, genre))
    #     # Выполняем запрос
    #     con.commit()
    #     print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
    for i, book in enumerate(books):
        print(f'book[0] = {book[0]}')
        # Готовим запрос в базу
        cur.execute(text_sql_book, (i+1, book[0], book[1], book[2], book[3], book[4]))
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