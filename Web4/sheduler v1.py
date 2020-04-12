import datetime

import schedule

sign = input('какое сообщение надо выводить в консоль вместо «Ку»\n')
time = input('Укажите диапазон времени в 24-часовом формате, когда '
             'кукушка должна молчать.\n Например, "00-07" или один час 11')


def time_off(hour):
    global time

    t = time.split('-')
    if len(t) > 1:
        t_off = [str(i) for i in range(int(time.split('-')[0]), int(time.split('-')[1]) + 1)]
    else:
        t_off = t
    if hour in t_off:
        return False
    else:
        return True


def job():
    global sign
    sign_loc = 'Ку'
    if sign != "":
        sign_loc = sign

    date = datetime.datetime.now()
    if time_off(date.strftime('%H')):
        for i in range(int(date.strftime('%I'))):
            print(f'{sign_loc}')


schedule.every().hour.do(job)

while True:
    schedule.run_pending()

