def palindrome():
    n = open("input.dat", 'rb')
    g = ''
    n.read()
    for i in n.read():
        g += str(i)
        print(g)
    if g == g[::-1]:
        return 'True'
    else:
        return 'False'


palindrome()