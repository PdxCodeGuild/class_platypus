import colorsys

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

r = (5)
g = (5)
b = (5)
# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/5, g/5, b/5)

# do some math on h, s, v

r, g, b = colorsys.hsv_to_rgb(0.2, 0.1, 0.1)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)

img.show()

#to desaturate image
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         Y = 0.299 * r + 0.587 * g + 0.114 * b
#         pixels[i, j] = (int(Y), int(Y), int(Y))