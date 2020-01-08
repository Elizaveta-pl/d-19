le = 0
mi = 0
pl = 0
zer = 0
h = 0
y = list(open('input.txt'))
for i in y:
    u = i.split()
    h = len(u)
    if u[0] != '0' and h != 1:
        for j in u:
            if int(j) < 0:
                mi += 1
            elif int(j) > 0:
                pl += 1
            else:
                zer += 1
    else:
        g = open('output.txt', "w")
        g.write('0')
        g.close()
g = open('output.txt', "w")
g.write(str(h) + '\n')
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
