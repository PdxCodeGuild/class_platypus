import colorsys

from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

r = 1
g = 1
b = 1

# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# do some math on h, s, v
h = 21
s = 255
v = 255
r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)

img.show()
