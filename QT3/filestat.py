g = list(open("input.txt"))
g_c = []
for i in g:
    g_c.append(i.split())
g.clear()
for h in g_c:
    for j in h:
        g.append(int(j))

print(g)