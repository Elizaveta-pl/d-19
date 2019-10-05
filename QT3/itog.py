f = list(open('prices.txt'))
itg = 0
if len(f) == 0:
    print('')
else:
    for i in f:
        g = i.split('\t')
        itg += float(g[1]) * float(g[2])
    print('%.2f' % itg)
