import sqlite3


def get_result(name):
    cor = sqlite3.connect(name)
    cur = cor.cursor()
    cur.execute("""delete FROM Films
                    WHERE title like 'Я%' and title like '%а'""")
    cor.commit()
    cor.close()
