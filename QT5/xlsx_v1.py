import xlrd
import csv


def readxlsx():
    workbook = xlrd.open_workbook('data.xlsx')

    for index in range(workbook.nsheets):
        sheet = workbook.sheet_by_index(index)
        data = [sheet.row_values(row, 0, sheet.ncols)
                for row in range(sheet.nrows)]
    saveToCsv(data)


def saveToCsv(data):
    outfile = open('output.csv', 'w')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    writer.writerows(data)
    outfile.close()


readxlsx()
