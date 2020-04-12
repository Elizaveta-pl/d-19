import datetime

import schedule


def job():
    date = datetime.datetime.now()
    for i in range(int(date.strftime('%I'))):
        print(f'Ку')


schedule.every().hour.do(job)

while True:
    schedule.run_pending()
