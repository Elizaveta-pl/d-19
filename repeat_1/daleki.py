import sys


def f_len(x):
    s = 0
    for line in x:
        line = line.replace('"', '')
        line = line.replace('(', '')
        if line.lower() in spisok_padeg_edins:
            s = 1
    if s == 1:
        scena.append(s)


scena = []
spisok_padeg_edins = ['далек', 'далека', 'далеку', 'далеком', 'далеке',
                      'далеки', 'далеков', 'далекам', 'далеками', 'далеках']

words = list(map(f_len, map(str.split, sys.stdin)))
print(len(scena))
