def reverse():
    f_w = open("output.dat", 'wb')
    f_w.write(open("input.dat", mode='rb')[::-1])


reverse()
