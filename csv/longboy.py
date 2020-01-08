import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""delete FROM Films
                    WHERE genre=11 and duration>=90""")
    cor.commit()
    cor.close()
