import sys

try:
    summ = 0
    int(sys.argv[1])
    t = [int(sys.argv[i]) for i in range(len(sys.argv)) if i != 0]
    for i in range(len(t)):
        if i % 2 != 0:
            summ -= t[i]
        else:
            summ += t[i]
    print(summ)
except ValueError:
    print('ValueError')
except IndexError:
    print('NO PARAMS')
