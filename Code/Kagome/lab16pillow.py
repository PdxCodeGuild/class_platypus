from PIL import Image, ImageEnhance

# the code below works and is much simpler :)
# image = Image.open('/Users/kagome/PycharmProjects/class_platypus/Code/Kagome/lena.png')
# greyscale_image = image.convert('L')
# greyscale_image.save('greyscale_image.jpg')

img = Image.open("lena.png")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = int(0.299 * r + 0.587 * g + 0.114 * b)
        pixels[i, j] = (y, y, y)
img.show()

# img = Image.open("lena.png")
# converter = ImageEnhance.Contrast(img)
# img2 = converter.enhance(0.0)
# img.show()


# img = Image.open("lena.png")
# width, height = img.size
# pixels = img.load()
# enhancer = ImageEnhance.Contrast('lena.png')
# image = enhancer.enhance(0.5)
# image.save('lena.png')


# image.save('lena.jpg') save it as a different file extension
# https://www.youtube.com/watch?v=6Qs3wObeWwc tutorial
