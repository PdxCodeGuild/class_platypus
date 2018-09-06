from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
print(width,height)
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        #Y = int(0.299 * r + 0.587 * g + 0.114 * b)#Luminosity method
        Y = int((r + g + b)/3)# Average method

        pixels[i, j] = (Y, Y, Y)

img.show()
