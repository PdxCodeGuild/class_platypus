# Image Manipulation
# By Skyler Parker
# Created on 17AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        print(Y)
        pixels[i, j] = (255, 255, 255)

img.show()
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Enter a new grade\n2 - Close Program'))
    if menu_answer == 1:
        pass
    else:
        break