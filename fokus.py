s = []
le = [0, 0]
ra = [0, 0]
bo = [0, 0]
to = [0, 0]
for i in range(int(input())):
    g = input()
    s.append(g.split())
for j in s:
    if int(j[0]) < le[0]:
        le = j

print(s)
