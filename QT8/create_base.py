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



def create_base():
    try:
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

        books = [['Мойдодыр', 'Чуковский Корней', 2016, 'Стихи', 1],
                 ['Айболит', 'Чуковский Корней', 2015, 'Стихи', 2],
                 ['Дед Мороз', 'Степанов В.', 2017, 'Стихи', 3],
                 ['Краденое солнце', 'Жигарев Вячеслав Алексеевич', 2010, 'Стихи', 4],
                 ['Гарри Поттер', 'Роулинг Джоан Кэтлин', 2018, 'Фэнтези', 5],
                 ['Девочка с Земли', 'Кир Булычев', 2016, 'Фэнтези', 6],
                 ['Блейз', 'Кинг Стивен', 2018, 'Фэнтези', 7],
                 ['Оно. Тень прошлого', 'Кинг Стивен', 2018, 'Фэнтези', 8],
                 ['Девушка в тумане', 'Карризи Донато', 2018, 'Детективы', 9],
                 ['Убийства по алфавиту', 'Кристи Агата', 2019, 'Детективы', 10],
                 ['Мотылек', 'Шарьер Анри', 2015, 'Романы', 11],
                 ['Трезориум', 'Борис Акунин', 2019, 'Романы', 12]
                 ]
        where_sql = 'title'
        where_sql_text = ''
        # Открываем базу данных
        con = sqlite3.connect('catalog_1.db')
        cur = con.cursor()
        # Получаем бинарные данные нашего файла
        # data = readImage("woman.jpg")
        # # Конвертируем данные
        # binary = sqlite3.Binary(data)

        # Готовим текст запроса в базу

        text_sql_base = f'CREATE TABLE "book" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `title` ' \
                        f'text NOT NULL, `autor` TEXT, `year` INTEGER NOT NULL, `genre` TEXT NOT NULL,' \
                        f' `photo` blob NOT NULL)'
        cur.execute(text_sql_base)
        con.commit()
        text_sql_genres = f'INSERT INTO genres VALUES (?,?)'
        text_sql_book = f'INSERT INTO book VALUES (?,?,?,?,?,?)'
        for i, book in enumerate(books):
            print(f'book[0] = {sqlite3.Binary(readImage(str(books_jpg[i])))}')
            # Готовим запрос в базу
            cur.execute(text_sql_book, (i + 1, book[0], book[1], book[2], book[3], sqlite3.Binary(readImage(str(books_jpg[i])))))
            # Выполняем запрос
            con.commit()
        cur.close()

    # В случаи ошибки выводим ее текст.
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if con:
            # Закрываем подключение с базой данных
            con.close()
            print("The SQLite connection is closed")


create_base()