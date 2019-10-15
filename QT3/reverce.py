
def reverse():
    f_w= open("output.dat", 'wb')
    for i in list(open("input.dat", mode='rb')):
        print(i)
        g = i[::-1]
        f_w.write(g)
    f_w.close()


reverse()
