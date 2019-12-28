import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""UPDATE films SET duration=duration*2
                        WHERE genre=8""").fetchall()
    cor.commit()
    cor.close()
