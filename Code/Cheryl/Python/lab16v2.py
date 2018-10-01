import colorsys
from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
r, g, b = colorsys.hsv_to_rgb(h, s, v)

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        pixels[i, j] = (int(Y), int(Y), int(Y))


r = int(r*255)
g = int(g*255)
b = int(b*255)

img.show()