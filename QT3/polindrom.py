def palindrome():
    n = open("input.dat", 'rb')
    g = n.read()
    ln = len(g) // 2
    if len(g) == 1:
        ln = 1
    elif len(g) == 0:
        return 'True'

    for i in range(ln):
        if g[i] != g[-1 - i]:
            return 'False'
        else:
            return 'True'
