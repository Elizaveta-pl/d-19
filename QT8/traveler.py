import sqlite3, random, sys


class Traveller:
    def __init__(self):
        pass

    def create_base(self):
        try:
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

            # Открываем базу данных
            con = sqlite3.connect('traveler.db')
            cur = con.cursor()

            # Готовим текст запроса в базу
            text_sql_base = f'CREATE TABLE "book" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `title` ' \
                            f'text NOT NULL, `autor` TEXT, `year` INTEGER NOT NULL, `genre` TEXT NOT NULL,' \
                            f' `photo` blob NOT NULL)'
            cur.execute(text_sql_base)
            con.commit()
            text_sql_genres = f'INSERT INTO genres VALUES (?,?)'
            text_sql_book = f'INSERT INTO book VALUES (?,?,?,?,?,?)'
            cur.close()

        # В случаи ошибки выводим ее текст.
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            if con:
                # Закрываем подключение с базой данных
                con.close()
                print("The SQLite connection is closed")

if __name__ == "__main__":
    ui = Traveller()
    ui.create_db()
# traveler