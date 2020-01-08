import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""UPDATE films SET duration='100'
                    WHERE genre=22 and duration>100""")
    cor.commit()
    cor.close()
