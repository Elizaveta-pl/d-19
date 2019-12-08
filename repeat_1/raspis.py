import sys

s = {}
words = list(map(str.strip, sys.stdin))
wordsgood = [x for x in words if
             x not in ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                       'Пятница', 'Суббота', '']]

for i in wordsgood:
    f = wordsgood[wordsgood.index(i)].split()
    if len(f) != 2:
        g = ' '.join(f[:-1])
        g1 = f[-1]
        f.clear()
    f.append(g)
        f.append(g1)
    if int(f[1]) in s:
        if s.get(int(f[1])) != f[0]:

            if f[0] in s.get(int(f[1])).split(', '):
                f[0] = s.get(int(f[1]))
            else:
                f[0] = s.get(int(f[1])) + ', ' + f[0]
    s.update({int(f[1]): f[0]})
list_keys = list(s.keys())

list_keys.sort()
for i in list_keys:
    print(f'{i}: {s[i]}')
