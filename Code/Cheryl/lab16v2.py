import colorsys

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        pixels[i, j] = (int(Y), int(Y), int(Y))
img.show()

# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# do some math on h, s, v

r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*25)
g = int(g*25)
b = int(b*25)