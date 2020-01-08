import xlrd
import csv
 # import xrange


def readxlsx():
    # Open in the workbook
    workbook = xlrd.open_workbook('data.xlsx')
    # Листов в книге
    print(workbook.nsheets)

    for index in range(workbook.nsheets):
        sheet = workbook.sheet_by_index(index)
        data = [sheet.row_values(row, 0, sheet.ncols)
                for row in range(sheet.nrows)]
    saveToCsv(data)
        # for row in range(sheet.nrows):
        #     print(sheet.row_values(row, 0, sheet.ncols))
        #     # print(sheet.row(1))

        # for crange in sheet.col_label_ranges:
        #     print(f'crange = {crange}')
        #     rlo, rhi, clo, chi = crange
        #     for rx in range(rlo, rhi):
        #         for cx in range(clo, chi):
        #             print( "Column label at (rowx=%d, colx=%d) is %r" \
        #                 (rx, cx, sheet.cell_value(rx, cx)))


    # Имена листов
    print(workbook.sheet_names())

    # Получить количество строк и в листе Excel
    num_rows = sheet.nrows
    # Получить количество столбцов в листе Excel
    num_col = sheet.ncols

    print(num_rows, num_col)


def saveToCsv(data):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        # Получение списка заголовков
        # writer.writerow([tableWidget.horizontalHeaderItem(i).text()
        #                  for i in range(tableWidget.columnCount())])
        # for i in range(tableWidget.rowCount()):
        #     row = []
        #     for j in range(tableWidget.columnCount()):
        #         item = tableWidget.item(i, j)
        #         if item is not None:
        #             row.append(item.text())
        #     writer.writerow(row)

    # for row in csv.reader(open('data.csv'), delimiter=','):
    #     print(row)

    # Write csv file
    # data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    outfile = open('output.csv', 'w')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    writer.writerows(data)
    outfile.close()

readxlsx()