import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT title FROM Films
                        WHERE duration >= 60 and genre=(SELECT id FROM genres'
                     ' WHERE  title = "комедия") """).fetchall()

for elem in result:
    print(elem[0])

con.close()