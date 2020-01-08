import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute('SELECT title FROM Films  WHERE'
                     ' (year >= 1997) AND (genre=(SELECT id FROM genres'
                     ' WHERE  title = "музыка") or'
                     ' genre=(SELECT id FROM genres'
                     ' WHERE title = "анимация"))').fetchall()

for elem in result:
    print(str(elem)[2:-3])

con.close()
