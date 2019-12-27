import csv
from operator import itemgetter

g, f = input().split()
g = g.zfill(2)
f = f.zfill(2)
i = []
with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in list(reader)[1::]:
        row = str(row)[1:-2].split(',')
        if row[2].split('-')[2] == g and row[2].split('-')[3] == f:
            i.append((row[1].split()[3], row[-1][1:-1]))
i.sort(reverse=True)
i.sort(key=itemgetter(1), reverse=True)
for j in i:
    print(j[0], j[1])