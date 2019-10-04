import random
g = list(open("lines.txt"))
if len(g) != 0:
    d = random.randrange(0, (len(g) - 1))
    print(g[d])
else:
    print('')
