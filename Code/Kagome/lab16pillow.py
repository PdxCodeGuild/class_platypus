from PIL import Image

#def edit_image():

image = Image.open('/Users/kagome/PycharmProjects/class_platypus/Code/Kagome/lena.png')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')


#     width, height = img.size
#     pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

