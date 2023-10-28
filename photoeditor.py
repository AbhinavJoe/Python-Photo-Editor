from PIL import Image, ImageEnhance, ImageFilter, ImageColor
import os

pathIn = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(pathIn):
    img = Image.open(f"{pathIn}/{filename}")

    # sharpen, BW, transform, rotate
    # Image tranform size set for sample device and image. Can be changed according to image and device.
    edit = img.filter(ImageFilter.SHARPEN).convert('L').transform(
        (1366, 768), Image.AFFINE, (1, 0, 0, 0, 1, 0)).rotate(0)

    # contrast
    factor = 2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
