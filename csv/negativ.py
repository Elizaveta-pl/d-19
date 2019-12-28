import csv

with open('proba.jpg', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in list(reader)[54::]:
        row = 255 - row
