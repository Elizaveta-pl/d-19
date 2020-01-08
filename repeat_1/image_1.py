from PIL import Image


def crop_image(original_image, cut_image, area):
    cropped_img = original_image.crop(area)
    cropped_img.save(cut_image)


original_image = Image.open("image.bmp")
width, height = original_image.size
step = 4
step_cut = int(width / step)
for i in range(step):
    for j in range(step):
        name = str(i + 1) + str(j + 1)
        if name != (str(step) + str(step)):
            area = (step_cut * j, step_cut * i,
                    step_cut * (j + 1), step_cut * (i + 1))
            cut_image = 'image' + name + '.bmp'
            crop_image(original_image, cut_image, area)
