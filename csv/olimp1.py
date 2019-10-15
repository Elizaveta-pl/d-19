import csv

g, f = input().split()
i = []
with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in list(reader)[1::]:
        row = str(row)[1:-2].split(',')
        if row[2].split('-')[2] == g and row[2].split('-')[3] == f:
            i.append(f'{row[1].split()[3]} {row[-1][1:-1]}')
i.sort(key=)