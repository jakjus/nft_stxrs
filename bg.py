import png
import random
import numpy as np
import io, json

amount = 4
size = (16, 16)

# Do you remember the sky when we first met? ... What?     Oh

full = []

i = 0

def getArray():
    image = []
    image.append([0]*size[0])
    for i in range(size[1]-2):
        row = []
        row.append(0)
        prevPixel = 0
        for j in range(size[0]-2):
            pixel = 0
            if prevPixel == 0 and image[i][j+1] == 0 and random.random() < 0.03:
                pixel = 255
            prevPixel = pixel
            row.append(pixel)
        row.append(0)
        image.append(row)
    image.append([0]*size[1])
    return image

def invert(image):
    if random.random() < 0.5:
        image.reverse()
        for row in image:
            row.reverse()
    return image

def generateFile(array):
    png.from_array(array, 'L').save("bg.png")

while i < amount:
    array = getArray()
    array = invert(array)
    if array in full:
        continue
    full.append(array)
    i = i+1

newfull = []
for array in full:
    for i_row in range(array):
        fullrow = []
        for j in range(full)
            fullrow.append(full[j][i_row])
        newfull.append(fullrow)

print(newfull)
