dict = {}
u = 0
itg = 0
cek = 1
prob = 0
for i in range(int(input())):
    f = input().split("\t")
    dict[f[0]] = f[-1]
g = input()
h = input()
while h != '.':
    while h != '' and h != '.':
        h = h.split('\t')
        c = int(dict.get(h[0])) * int(h[-1])
        u += c
        h = input()
        if h == '' or h == '.':
            print(f'{cek}) {u}')
            itg += u
            cek += 1
    u = 0
    c = 0
    prob += 1
    if h != '.':
        h = input()

itg += u
print(f'Итого: {itg}')
