
text = list(open('input_test.txt'))
# zamena = input().split(' ')
zamena = '* s -- —'.split(' ')
# print(f'zamena = {zamena}')
#s_in = str(zamena[2])
#s_out = str(zamena[3])

s_in = '--'
s_out = '-'

g = open('output_tst.txt', "w")

for i in text:
    g.write(i.replace(s_in, s_out) + '\n')


g.close()