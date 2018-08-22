from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = 2 * r + 1* g + .3 * b
        y = int(y)
        pixels[i, j] = (y, y, y)


img.show()