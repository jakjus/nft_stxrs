import png
from utils.image import *
from utils.metadata import *

amount = 4 # number of rectangles in a row
size = (16, 16) # single rectangle in a row

# Do you remember the sky when we first met? ... What?     Oh

full = []

i = 0

while i < amount:
    array = getArray(size)
    array = invert(array)
    if array in full:
        continue
    full.append(array)
    i = i+1

newfull = []
for i_row in range(len(array)):
    fullrow = []
    for j in range(len(full)):
        fullrow += full[j][i_row]
    newfull.append(fullrow)

png.from_array(newfull, 'L').save("bg.png")
