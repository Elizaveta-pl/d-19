import csv

put = []
with open('input.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    reader = list(reader)
    n, k, c = reader[-1]
    reader = reader[:-1]
    reader.sort(key=lambda s: int(s[2]))
    for row in reader:
        if n == row[0] and k == row[1]:
            put.append(row[0])
            put.append(row[1])
            n = row[0]
            k = row[1]
            break
        elif n == row[0]:
            put.append(row[0])
            put.append(row[1])
            n = row[0]
            k = row[1]
            break
    for e in list(reader):
        if k == e[0]:
            put.append(e[1])
            break
print(' '.join(put))
