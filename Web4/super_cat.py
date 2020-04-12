import sys

try:
    if '--sort' in sys.argv:
        pass
    file = [sys.argv[i] for i in range(len(sys.argv)) if sys.argv[i].find('.txt') != -1]
    f = open(file[0], encoding="utf8")
    text = [i.rstrip() for i in f]
    if '--sort' in sys.argv:
        text = sorted(text)
    j = 0
    for i in text:
        if '--num' in sys.argv:
            print(f'{j} {i}')
            j += 1
        else:
            print(f'{i}')
    if '--count' in sys.argv:
        print(f'rows count: {len(text)}')
    f.close()

except ValueError:
    print('ValueError')
except IndexError:
    print('ERROR')
except FileNotFoundError:
    print('ERROR')
