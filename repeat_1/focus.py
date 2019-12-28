from PIL import Image
import numpy as np
from collections import Counter
from numpy import array
    # as np

original_image = Image.open('tests/res2.png')

w, h = original_image.size
rr, gg, bb = 0, 0, 0

rgb_im = original_image.convert('RGB')
data = np.array(rgb_im)
print(f'data0 ={data[1].shape}')
array = ["Bob", "Alex", "Bob", "John"]
# c = Counter(data[0])
# # d = tuple(data)
# print(f'c = {c}, data =')
d = []

b, g, r = rgb_im.split()
# print(f' data = {data[0]} type = {type(data)}')
print(f' size = {data.shape}, g = {g}, r = {r}')

for x in range(w):
    for y in range(h):
        r, g, b = original_image.getpixel((x, y))
        d.append(original_image.getpixel((x, y)))
d1 = tuple(d)
print(original_image.getpixel((x, y)))
        # print(f' r = {r}, g = {g}, b = {b}')
        # rr += r
        # gg += g
        # hh += h
print(f'd1 = {d1}')
#
# cnt = w * h
# print(rr // cnt, gg / cnt, hh // cnt)