le = 0
mi = 0
pl = 0
zer = 0
g = open('output.txt', "w")
for i in list(open('input.txt')):
    i = i.split()
    for j in i:
        if j != '0' and len(i) > 1:
            le += 1
            if int(j) < 0:
                mi += 1
            elif int(j) > 0:
                pl += 1
            else:
                zer += 1
        else:
            g.write('0')
            g.close()
g = open('output.txt', "w")
g.write(str(le) + '\n')
if mi == 0 and pl == 0 and zer == 0:
    pass
elif mi == 0 and pl == 0:
    g.write(f'0 {zer}')
elif mi == 0 and zer == 0:
    g.write(f'1 {pl}')
elif pl == 0 and zer == 0:
    g.write(f'-1 {mi}')
elif mi == 0:
    g.write(f'1 {pl} 0 {zer}')
elif pl == 0:
    g.write(f'-1 {mi} 0 {zer}')
elif zer == 0:
    g.write(f'1 {pl} -1 {mi}')
else:
    g.write(f'1 {pl} -1 {mi} 0 {zer}')
