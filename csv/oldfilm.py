import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""UPDATE films SET duration=duration/3 WHERE year=1973""")
    cor.commit()
    cor.close()
