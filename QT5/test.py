import sys, csv

with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    result = []
    result1 = []
    result_new = []
    row_new = []
    shool1 = ''
    klass1 = '09'
    for row in list(reader)[1:]:
        print(f'row= {row}')
        row_new = []
        row_new.append(row[0])
        row_new.append(f'{row[1].split()[3]} {row[1].split()[4]}')
        row_new.append(row[2])
        row_new.append(row[7])


        row.append(row[2].split('-')[2])
        row.append(row[2].split('-')[3])

        # print(row[2].split('-')[2])
        # print(row[2].split('-')[3])
        result.append(row)
        result_new.append(row_new)
        if row[9] == shool1:
            result1.append(row)
        if klass1 == '' and shool1 == '':
            result1 = [row for row in result]
        elif klass1 == '':
            result1 = [row for row in result if row[8] == shool1]
        elif shool1 == '':
            result1 = [row for row in result if row[9] == klass1]
        else:
            result1 = [row for row in result if
                       (row[8] == shool1 or row[9] == klass1)]

        # for row in result:
        #     if row[9] == shool1:
        #         result1.append(row)
        #
        # print(row)
    # print(f'result = {result}')
    print(f'result1_len = {len(result1)}')
    print(f'result_new = {result_new}')
    login = [row[2].split('-') for row in result]
    fio = [row[1].split() for row in result]
    shool = [i[2] for i in login]
    klass = [i[3] for i in login]
    klass.append('')
    shool.append('')
    shool = list(set(shool))
    klass = list(set(klass))
    # for row in list(reader):
    #     print(row[2])
    #     login = row[2].split('-')
    #     shool = 1
    #     klass = 2
    print(sorted(shool), sorted(klass))

    print(f'fio = {fio}')