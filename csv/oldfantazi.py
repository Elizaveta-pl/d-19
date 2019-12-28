import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""delete FROM Films
                    WHERE genre=8 and duration>90 and year < 2000""")
    cor.commit()
    cor.close()
